"""
Food Calorie Tracker Views
APIs for managing daily food entries and calorie tracking
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta, date
from .models import UserLogin, UserProfile, FoodItem, FoodEntry


@csrf_exempt
def search_foods(request):
    """
    Search for food items by name, category, or diet type
    GET params: query, category (optional), diet_type (optional), limit (default: 50)
    """
    if request.method == 'GET':
        try:
            query = request.GET.get('query', '').strip()
            category = request.GET.get('category', '')
            diet_type = request.GET.get('diet_type', '')
            limit = int(request.GET.get('limit', 50))
            
            if not query:
                return JsonResponse({
                    'success': False,
                    'message': 'Query parameter is required'
                }, status=400)
            
            # Build query
            foods = FoodItem.objects.filter(name__icontains=query)
            
            if category:
                foods = foods.filter(food_category=category)
            
            if diet_type:
                foods = foods.filter(diet_type=diet_type)
            
            foods = foods[:limit]
            
            foods_data = []
            for food in foods:
                foods_data.append({
                    'id': food.id,
                    'name': food.name,
                    'category': food.food_category,
                    'diet_type': food.diet_type,
                    'calories_per_100g': float(food.calories),
                    'protein': float(food.protein),
                    'carbs': float(food.carbs),
                    'fats': float(food.fats),
                    'serving_size': food.serving_size
                })
            
            return JsonResponse({
                'success': True,
                'foods': foods_data,
                'total': len(foods_data)
            }, status=200)
            
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
def get_food_categories(request):
    """Get all food categories"""
    if request.method == 'GET':
        try:
            categories = FoodItem.FOOD_CATEGORIES
            diet_types = FoodItem.DIET_TYPES
            meal_types = FoodEntry.MEAL_TYPE_CHOICES
            
            return JsonResponse({
                'success': True,
                'categories': [{'value': cat[0], 'label': cat[1]} for cat in categories],
                'diet_types': [{'value': dt[0], 'label': dt[1]} for dt in diet_types],
                'meal_types': [{'value': mt[0], 'label': mt[1]} for mt in meal_types]
            }, status=200)
            
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
def add_food_entry(request):
    """
    Add a food entry for user's daily food intake
    POST params:
    {
        "user_id": int,
        "food_item_id": int or null,
        "food_name": str (optional, for custom foods),
        "quantity": float,
        "quantity_unit": str (g, ml, piece, cup, bowl, etc.),
        "meal_type": str (breakfast, lunch, dinner, snacks, fruits, nuts, milks, other),
        "entry_date": "YYYY-MM-DD",
        "custom_calories": float (optional, for custom foods)
    }
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            food_item_id = data.get('food_item_id')
            food_name = data.get('food_name', '')
            quantity = data.get('quantity')
            quantity_unit = data.get('quantity_unit', 'g')
            meal_type = data.get('meal_type')
            entry_date_str = data.get('entry_date')
            custom_calories = data.get('custom_calories')
            
            # Validate required fields
            if not user_id or not quantity or not meal_type or not entry_date_str:
                return JsonResponse({
                    'success': False,
                    'message': 'user_id, quantity, meal_type, and entry_date are required'
                }, status=400)
            
            # Parse entry date
            try:
                entry_date = datetime.strptime(entry_date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid entry_date format. Use YYYY-MM-DD'
                }, status=400)
            
            # Check if user exists
            try:
                user = UserLogin.objects.get(id=user_id)
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            
            # Get or create food item
            if food_item_id:
                try:
                    food_item = FoodItem.objects.get(id=food_item_id)
                except FoodItem.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'message': 'Food item not found'
                    }, status=404)
            else:
                # Create custom food item
                if not food_name:
                    return JsonResponse({
                        'success': False,
                        'message': 'food_name is required for custom foods'
                    }, status=400)
                
                if not custom_calories:
                    return JsonResponse({
                        'success': False,
                        'message': 'custom_calories is required for custom foods'
                    }, status=400)
                
                # Create food item with custom calories (fixed default)
                food_item, created = FoodItem.objects.get_or_create(
                    name=food_name,
                    defaults={
                        'food_category': 'other',
                        'diet_type': 'vegan',
                        'calories': custom_calories,
                        'protein': 0,
                        'carbs': 0,
                        'fats': 0,
                        'serving_size': quantity_unit
                    }
                )
            
            # Create food entry
            food_entry = FoodEntry.objects.create(
                user=user,
                food_item=food_item,
                quantity=quantity,
                quantity_unit=quantity_unit,
                meal_type=meal_type,
                entry_date=entry_date,
                is_custom_calories=bool(custom_calories)
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Food entry added successfully',
                'entry': {
                    'id': food_entry.id,
                    'food_name': food_item.name,
                    'quantity': food_entry.quantity,
                    'quantity_unit': food_entry.quantity_unit,
                    'meal_type': food_entry.meal_type,
                    'calculated_calories': float(food_entry.calculated_calories),
                    'entry_date': food_entry.entry_date.strftime('%Y-%m-%d')
                }
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)


@csrf_exempt
def get_daily_food_entries(request):
    """
    Get all food entries for a specific date
    GET params: user_id, date (YYYY-MM-DD)
    """
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            date_str = request.GET.get('date')
            
            if not user_id or not date_str:
                return JsonResponse({
                    'success': False,
                    'message': 'user_id and date parameters are required'
                }, status=400)
            
            # Parse date
            try:
                entry_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid date format. Use YYYY-MM-DD'
                }, status=400)
            
            # Check if user exists
            try:
                user = UserLogin.objects.get(id=user_id)
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            
            # Get daily entries
            entries = FoodEntry.objects.filter(user=user, entry_date=entry_date).order_by('meal_type', '-created_at')
            
            entries_data = []
            for entry in entries:
                entries_data.append({
                    'id': entry.id,
                    'food_name': entry.food_item.name,
                    'category': entry.food_item.food_category,
                    'quantity': entry.quantity,
                    'quantity_unit': entry.quantity_unit,
                    'meal_type': entry.meal_type,
                    'calculated_calories': float(entry.calculated_calories),
                    'created_at': entry.created_at.strftime('%Y-%m-%d %H:%M:%S')
                })
            
            # Get daily breakdown and total
            daily_total = FoodEntry.get_daily_total(user, entry_date)
            daily_breakdown = FoodEntry.get_daily_breakdown(user, entry_date)
            
            # Get user's calorie target from profile
            user_calorie_target = 0
            try:
                profile = UserProfile.objects.get(user=user)
                calorie_data = profile.calculate_target_calories()
                user_calorie_target = calorie_data['target_calories']
            except:
                pass
            
            return JsonResponse({
                'success': True,
                'date': entry_date.strftime('%Y-%m-%d'),
                'entries': entries_data,
                'daily_summary': {
                    'total_calories': float(daily_total),
                    'calorie_target': user_calorie_target,
                    'remaining_calories': float(user_calorie_target - daily_total) if user_calorie_target > 0 else 0,
                    'breakdown': {meal_type: breakdown for meal_type, breakdown in daily_breakdown.items()}
                }
            }, status=200)
            
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
def get_food_history(request):
    """
    Get food entries history for a date range
    GET params: user_id, start_date (optional, YYYY-MM-DD), end_date (optional, YYYY-MM-DD), days (default: 30)
    """
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            start_date_str = request.GET.get('start_date')
            end_date_str = request.GET.get('end_date')
            days = int(request.GET.get('days', 30))
            
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'user_id parameter is required'
                }, status=400)
            
            # Check if user exists
            try:
                user = UserLogin.objects.get(id=user_id)
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            
            # Determine date range
            if end_date_str:
                try:
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                except ValueError:
                    return JsonResponse({
                        'success': False,
                        'message': 'Invalid end_date format. Use YYYY-MM-DD'
                    }, status=400)
            else:
                end_date = date.today()
            
            if start_date_str:
                try:
                    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                except ValueError:
                    return JsonResponse({
                        'success': False,
                        'message': 'Invalid start_date format. Use YYYY-MM-DD'
                    }, status=400)
            else:
                start_date = end_date - timedelta(days=days)
            
            # Get entries in date range
            entries = FoodEntry.objects.filter(
                user=user,
                entry_date__gte=start_date,
                entry_date__lte=end_date
            ).order_by('-entry_date', 'meal_type')
            
            # Group by date
            daily_data = {}
            for entry in entries:
                date_key = entry.entry_date.strftime('%Y-%m-%d')
                if date_key not in daily_data:
                    daily_data[date_key] = {
                        'date': date_key,
                        'total_calories': 0,
                        'entries': [],
                        'breakdown': {}
                    }
                
                daily_data[date_key]['entries'].append({
                    'id': entry.id,
                    'food_name': entry.food_item.name,
                    'meal_type': entry.meal_type,
                    'quantity': entry.quantity,
                    'quantity_unit': entry.quantity_unit,
                    'calories': float(entry.calculated_calories)
                })
                daily_data[date_key]['total_calories'] += float(entry.calculated_calories)
            
            # Calculate breakdown for each day
            for date_key in daily_data:
                entry_date_obj = datetime.strptime(date_key, '%Y-%m-%d').date()
                breakdown = FoodEntry.get_daily_breakdown(user, entry_date_obj)
                daily_data[date_key]['breakdown'] = breakdown
            
            # Convert to list and sort by date
            history_list = sorted(daily_data.values(), key=lambda x: x['date'], reverse=True)
            
            # Calculate statistics
            total_days = len(history_list)
            total_calories = sum([day['total_calories'] for day in history_list])
            avg_daily_calories = total_calories / total_days if total_days > 0 else 0
            max_calories = max([day['total_calories'] for day in history_list]) if history_list else 0
            min_calories = min([day['total_calories'] for day in history_list]) if history_list else 0
            
            # Get user's calorie target
            user_calorie_target = 0
            try:
                profile = UserProfile.objects.get(user=user)
                calorie_data = profile.calculate_target_calories()
                user_calorie_target = calorie_data['target_calories']
            except:
                pass
            
            return JsonResponse({
                'success': True,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'daily_history': history_list,
                'statistics': {
                    'total_days': total_days,
                    'total_calories': float(total_calories),
                    'average_daily_calories': float(avg_daily_calories),
                    'max_daily_calories': float(max_calories),
                    'min_daily_calories': float(min_calories),
                    'calorie_target': user_calorie_target,
                    'days_above_target': sum([1 for day in history_list if day['total_calories'] > user_calorie_target])
                }
            }, status=200)
            
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
def delete_food_entry(request):
    """Delete a food entry by id"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            entry_id = data.get('entry_id')
            user_id = data.get('user_id')
            
            if not entry_id or not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'entry_id and user_id are required'
                }, status=400)
            
            try:
                entry = FoodEntry.objects.get(id=entry_id, user_id=user_id)
                entry.delete()
                
                return JsonResponse({
                    'success': True,
                    'message': 'Food entry deleted successfully'
                }, status=200)
                
            except FoodEntry.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Food entry not found'
                }, status=404)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)
