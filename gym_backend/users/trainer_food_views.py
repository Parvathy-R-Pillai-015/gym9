"""
Trainer Food Calorie Tracking Views
APIs for trainers to view assigned users' daily food entries and calorie tracking
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta, date
from .models import UserLogin, UserProfile, FoodItem, FoodEntry, Trainer


@csrf_exempt
def trainer_get_assigned_users_calories(request):
    """
    Get daily calorie summary for all users assigned to a trainer
    GET params: trainer_id, date (optional, default: today)
    Returns: List of assigned users with their daily calorie totals
    """
    if request.method == 'GET':
        try:
            trainer_id = request.GET.get('trainer_id')
            target_date_str = request.GET.get('date', str(date.today()))
            
            if not trainer_id:
                return JsonResponse({
                    'success': False,
                    'message': 'trainer_id is required'
                }, status=400)
            
            try:
                target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid date format. Use YYYY-MM-DD'
                }, status=400)
            
            try:
                trainer = Trainer.objects.get(id=trainer_id)
                
                # Get all users assigned to this trainer
                assigned_users = UserProfile.objects.filter(
                    assigned_trainer=trainer,
                    payment_status=True
                ).select_related('user')
                
                users_calories = []
                for profile in assigned_users:
                    user = profile.user
                    
                    # Get all food entries for this user on the target date
                    entries = FoodEntry.objects.filter(
                        user=user,
                        entry_date=target_date
                    )
                    
                    total_calories = sum(entry.calculated_calories for entry in entries)
                    
                    # Get breakdown by meal type
                    meal_breakdown = {}
                    for entry in entries:
                        meal_type = entry.meal_type
                        if meal_type not in meal_breakdown:
                            meal_breakdown[meal_type] = 0
                        meal_breakdown[meal_type] += entry.calculated_calories
                    
                    # Get personalized calorie target
                    calorie_target_info = profile.calculate_target_calories()
                    target_calories = calorie_target_info['target_calories']
                    
                    user_data = {
                        'user_id': user.id,
                        'user_name': user.name,
                        'user_email': user.emailid,
                        'total_calories': round(total_calories, 2),
                        'target_calories': target_calories,
                        'percentage': round((total_calories / target_calories * 100), 2) if target_calories > 0 else 0,
                        'remaining_calories': max(0, target_calories - total_calories),
                        'meal_breakdown': meal_breakdown,
                        'entry_count': len(entries),
                        'date': target_date_str
                    }
                    users_calories.append(user_data)
                
                # Sort by calories (highest first)
                users_calories.sort(key=lambda x: x['total_calories'], reverse=True)
                
                return JsonResponse({
                    'success': True,
                    'users': users_calories,
                    'total_users': len(users_calories),
                    'date': target_date_str
                }, status=200)
                
            except Trainer.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Trainer not found'
                }, status=404)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
                }, status=500)
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def trainer_get_user_daily_calories(request):
    """
    Get detailed daily calorie data for a specific user (trainer can view assigned users)
    GET params: trainer_id, user_id, date (optional, default: today)
    Returns: Detailed food entries with calorie breakdown
    """
    if request.method == 'GET':
        try:
            trainer_id = request.GET.get('trainer_id')
            user_id = request.GET.get('user_id')
            target_date_str = request.GET.get('date', str(date.today()))
            
            if not trainer_id or not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'trainer_id and user_id are required'
                }, status=400)
            
            try:
                target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid date format. Use YYYY-MM-DD'
                }, status=400)
            
            try:
                trainer = Trainer.objects.get(id=trainer_id)
                user = UserLogin.objects.get(id=user_id)
                
                # Verify that this user is assigned to this trainer
                try:
                    profile = UserProfile.objects.get(user=user, assigned_trainer=trainer)
                except UserProfile.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'message': 'User is not assigned to this trainer'
                    }, status=403)
                
                # Get all food entries for this user on the target date
                try:
                    entries = FoodEntry.objects.filter(
                        user=user,
                        entry_date=target_date
                    ).order_by('meal_type', '-created_at')
                    print(f"DEBUG: Found {len(entries)} entries for user {user_id} on {target_date}")
                except Exception as e:
                    print(f"ERROR fetching entries: {str(e)}")
                    raise
                
                entries_data = []
                for entry in entries:
                    try:
                        entry_data = {
                            'id': entry.id,
                            'food_name': entry.food_item.name if entry.food_item else 'Custom Food',
                            'meal_type': entry.meal_type,
                            'quantity': entry.quantity,
                            'quantity_unit': entry.quantity_unit,
                            'calories': round(entry.calculated_calories, 2),
                            'entry_time': entry.created_at.strftime('%H:%M') if entry.created_at else '',
                            'is_custom': entry.is_custom_calories
                        }
                        entries_data.append(entry_data)
                    except Exception as e:
                        print(f"Error processing entry {entry.id}: {str(e)}")
                        continue
                
                # Group by meal type
                meal_breakdown = {}
                for entry in entries:
                    meal_type = entry.meal_type
                    if meal_type not in meal_breakdown:
                        meal_breakdown[meal_type] = 0.0
                    meal_breakdown[meal_type] += entry.calculated_calories
                
                # Round meal breakdown values
                meal_breakdown = {k: round(v, 2) for k, v in meal_breakdown.items()}
                
                total_calories = sum(entry.calculated_calories for entry in entries)
                calorie_target_info = profile.calculate_target_calories()
                target_calories = calorie_target_info['target_calories']
                
                return JsonResponse({
                    'success': True,
                    'user_id': user.id,
                    'user_name': user.name,
                    'date': target_date_str,
                    'total_calories': round(total_calories, 2),
                    'target_calories': target_calories,
                    'percentage': round((total_calories / target_calories * 100), 2) if target_calories > 0 else 0,
                    'remaining_calories': max(0, target_calories - total_calories),
                    'entries': entries_data,
                    'meal_breakdown': meal_breakdown,
                    'entry_count': len(entries)
                }, status=200)
                
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            except Trainer.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Trainer not found'
                }, status=404)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
                }, status=500)
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def trainer_get_user_calorie_history(request):
    """
    Get 30-day calorie history for a user assigned to a trainer
    GET params: trainer_id, user_id
    Returns: Daily calorie data for last 30 days with statistics
    """
    if request.method == 'GET':
        try:
            trainer_id = request.GET.get('trainer_id')
            user_id = request.GET.get('user_id')
            
            if not trainer_id or not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'trainer_id and user_id are required'
                }, status=400)
            
            try:
                trainer = Trainer.objects.get(id=trainer_id)
                user = UserLogin.objects.get(id=user_id)
                
                # Verify that this user is assigned to this trainer
                try:
                    profile = UserProfile.objects.get(user=user, assigned_trainer=trainer)
                except UserProfile.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'message': 'User is not assigned to this trainer'
                    }, status=403)
                
                # Get last 30 days of data
                today = date.today()
                start_date = today - timedelta(days=30)
                
                entries = FoodEntry.objects.filter(
                    user=user,
                    entry_date__gte=start_date,
                    entry_date__lte=today
                )
                
                # Aggregate by date
                history = {}
                for entry in entries:
                    date_str = entry.entry_date.strftime('%Y-%m-%d')
                    if date_str not in history:
                        history[date_str] = {
                            'date': date_str,
                            'total_calories': 0,
                            'entries': []
                        }
                    history[date_str]['total_calories'] += entry.calculated_calories
                    history[date_str]['entries'].append({
                        'food_name': entry.food_item.name if entry.food_item else 'Custom Food',
                        'meal_type': entry.meal_type,
                        'calories': round(entry.calculated_calories, 2)
                    })
                
                # Sort by date descending
                sorted_history = sorted(history.items(), key=lambda x: x[0], reverse=True)
                history_list = [item[1] for item in sorted_history]
                
                # Calculate statistics
                if history_list:
                    calories_list = [h['total_calories'] for h in history_list]
                    avg_calories = sum(calories_list) / len(calories_list)
                    max_calories = max(calories_list)
                    min_calories = min(calories_list)
                else:
                    avg_calories = max_calories = min_calories = 0
                
                calorie_target_info = profile.calculate_target_calories()
                target_calories = calorie_target_info['target_calories']
                
                return JsonResponse({
                    'success': True,
                    'user_id': user.id,
                    'user_name': user.name,
                    'history': history_list,
                    'statistics': {
                        'total_days': len(history_list),
                        'average_calories': round(avg_calories, 2),
                        'max_calories': round(max_calories, 2),
                        'min_calories': round(min_calories, 2),
                        'target_calories': target_calories
                    }
                }, status=200)
                
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            except Trainer.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Trainer not found'
                }, status=404)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
                }, status=500)
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)
