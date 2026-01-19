from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from .models import UserLogin, Trainer, UserProfile, Attendance, Review, FoodItem, DietPlanTemplate, UserDietPlan

# Create your views here.

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            emailid = data.get('emailid')
            password = data.get('password')
            
            if not name or not emailid or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'All fields (name, emailid, password) are required'
                }, status=400)
            
            # Check if user with this email already exists
            if UserLogin.objects.filter(emailid=emailid).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'User with this email already exists'
                }, status=400)
            
            # Create new user
            user = UserLogin.objects.create(
                name=name,
                emailid=emailid,
                password=password  # Password will be hashed in the model's save method
            )
            
            return JsonResponse({
                'success': True,
                'message': 'User registered successfully',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'emailid': user.emailid
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
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            emailid = data.get('emailid')
            password = data.get('password')
            
            print(f"[LOGIN ATTEMPT] Email: {emailid}")  # Debug log
            
            if not emailid or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Email and password are required'
                }, status=400)
            
            # Find user by emailid
            try:
                user = UserLogin.objects.get(emailid=emailid)
                print(f"[USER FOUND] Name: {user.name}, Email: {user.emailid}")  # Debug log
            except UserLogin.DoesNotExist:
                print(f"[USER NOT FOUND] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'User not registered. Please register first.'
                }, status=401)
            
            # Check if user is active
            if not user.is_active:
                print(f"[INACTIVE USER] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'Account is inactive. Please contact support.'
                }, status=401)
            
            # Check password
            if user.check_password(password):
                print(f"[LOGIN SUCCESS] Email: {emailid} - Role: {user.role}")  # Debug log
                
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'emailid': user.emailid,
                    'role': user.role
                }
                
                # If user is a trainer, include trainer_id
                if user.role == 'trainer':
                    try:
                        trainer = Trainer.objects.get(user=user)
                        user_data['trainer_id'] = trainer.id
                    except Trainer.DoesNotExist:
                        pass
                
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',
                    'user': user_data
                }, status=200)
            else:
                print(f"[WRONG PASSWORD] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid email or password'
                }, status=401)
            
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
def create_trainer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            emailid = data.get('emailid')
            mobile = data.get('mobile')
            gender = data.get('gender')
            experience = data.get('experience')
            specialization = data.get('specialization')
            joining_period = data.get('joining_period')
            password = data.get('password')
            
            if not all([name, emailid, mobile, gender, experience, specialization, joining_period, password]):
                return JsonResponse({'success': False, 'message': 'All fields are required'}, status=400)
            
            if UserLogin.objects.filter(emailid=emailid).exists():
                return JsonResponse({'success': False, 'message': 'Email already exists'}, status=400)
            
            if len(mobile) != 10 or not mobile.isdigit():
                return JsonResponse({'success': False, 'message': 'Mobile number must be 10 digits'}, status=400)
            
            user = UserLogin.objects.create(name=name, emailid=emailid, password=password, role='trainer')
            trainer = Trainer.objects.create(user=user, mobile=mobile, gender=gender, experience=int(experience), specialization=specialization, joining_period=joining_period)
            
            return JsonResponse({'success': True, 'message': 'Trainer added successfully', 'trainer': {'id': trainer.id, 'name': user.name, 'emailid': user.emailid, 'mobile': trainer.mobile, 'specialization': trainer.specialization}}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False, 'message': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def create_profile(request):
    """Create or update user profile with fitness goals"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            
            # Validate user_id
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'User ID is required'
                }, status=400)
            
            # Check if user exists
            try:
                user = UserLogin.objects.get(id=user_id)
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            
            # Get all required fields
            mobile_number = data.get('mobile_number', '')
            age = data.get('age')
            gender = data.get('gender')
            current_weight = data.get('current_weight')
            current_height = data.get('current_height')
            goal = data.get('goal')
            target_weight = data.get('target_weight')
            target_months = data.get('target_months')
            workout_time = data.get('workout_time')
            diet_preference = data.get('diet_preference')
            food_allergies = data.get('food_allergies', '')
            health_conditions = data.get('health_conditions', '')
            trainer_id = data.get('trainer_id')
            
            # Validate required fields
            if not all([age, gender, current_weight, current_height, goal, target_weight, target_months, workout_time, diet_preference]):
                return JsonResponse({
                    'success': False,
                    'message': 'All fields are required except food allergies and health conditions'
                }, status=400)
            
            # Calculate payment amount based on target months
            payment_map = {1: 399, 2: 499, 3: 699, 6: 1199, 8: 1599, 12: 2199}
            payment_amount = payment_map.get(int(target_months), 0)
            
            # Check if profile already exists and update or create
            try:
                profile = UserProfile.objects.get(user=user)
                # Update existing profile
                profile.mobile_number = mobile_number
                profile.age = int(age)
                profile.gender = gender
                profile.current_weight = float(current_weight)
                profile.current_height = float(current_height)
                profile.goal = goal
                profile.target_weight = float(target_weight)
                profile.target_months = int(target_months)
                profile.workout_time = workout_time
                profile.diet_preference = diet_preference
                profile.food_allergies = food_allergies
                profile.health_conditions = health_conditions
                profile.payment_amount = payment_amount
                
                # Assign trainer if provided
                if trainer_id:
                    try:
                        trainer = Trainer.objects.get(id=trainer_id)
                        profile.assigned_trainer = trainer
                    except Trainer.DoesNotExist:
                        pass
                
                profile.save()
            except UserProfile.DoesNotExist:
                # Get trainer if provided
                assigned_trainer = None
                if trainer_id:
                    try:
                        assigned_trainer = Trainer.objects.get(id=trainer_id)
                    except Trainer.DoesNotExist:
                        pass
                
                # Create new profile with all fields
                profile = UserProfile.objects.create(
                    user=user,
                    mobile_number=mobile_number,
                    age=int(age),
                    gender=gender,
                    current_weight=float(current_weight),
                    current_height=float(current_height),
                    goal=goal,
                    target_weight=float(target_weight),
                    target_months=int(target_months),
                    workout_time=workout_time,
                    diet_preference=diet_preference,
                    food_allergies=food_allergies,
                    health_conditions=health_conditions,
                    payment_amount=payment_amount,
                    assigned_trainer=assigned_trainer
                )
            
            return JsonResponse({
                'success': True,
                'message': 'Profile saved successfully',
                'profile': {
                    'id': profile.id,
                    'user_id': user.id,
                    'age': profile.age,
                    'gender': profile.gender,
                    'current_weight': profile.current_weight,
                    'current_height': profile.current_height,
                    'goal': profile.goal,
                    'target_weight': profile.target_weight,
                    'target_months': profile.target_months,
                    'workout_time': profile.workout_time,
                    'diet_preference': profile.diet_preference,
                    'food_allergies': profile.food_allergies,
                    'health_conditions': profile.health_conditions,
                    'payment_amount': profile.payment_amount,
                    'payment_status': profile.payment_status
                }
            }, status=200)
            
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
def get_profile(request, user_id):
    """Get user profile by user_id"""
    if request.method == 'GET':
        try:
            print(f"Getting profile for user_id: {user_id}")
            user = UserLogin.objects.get(id=user_id)
            try:
                profile = UserProfile.objects.get(user=user)
                print(f"Profile found: {profile.id}, payment_status: {profile.payment_status}")
                
                # Get trainer info if assigned
                trainer_info = None
                if profile.assigned_trainer:
                    trainer = profile.assigned_trainer
                    trainer_info = {
                        'id': trainer.id,
                        'name': trainer.user.name,
                        'email': trainer.user.emailid,
                        'mobile': trainer.mobile,
                        'experience': trainer.experience,
                        'specialization': trainer.specialization,
                        'certification': trainer.certification or 'Not Specified'
                    }
                
                response_data = {
                    'success': True,
                    'profile': {
                        'id': profile.id,
                        'user_id': user.id,
                        'mobile_number': profile.mobile_number,
                        'age': profile.age,
                        'gender': profile.gender,
                        'current_weight': profile.current_weight,
                        'current_height': profile.current_height,
                        'goal': profile.goal,
                        'target_weight': profile.target_weight,
                        'target_months': profile.target_months,
                        'workout_time': profile.workout_time,
                        'diet_preference': profile.diet_preference,
                        'food_allergies': profile.food_allergies,
                        'health_conditions': profile.health_conditions,
                        'payment_amount': profile.payment_amount,
                        'payment_status': profile.payment_status,
                        'assigned_trainer': trainer_info
                    }
                }
                print(f"Returning response: {response_data}")
                return JsonResponse(response_data, status=200)
            except UserProfile.DoesNotExist:
                print(f"Profile not found for user_id: {user_id}")
                return JsonResponse({
                    'success': False,
                    'message': 'Profile not found'
                }, status=404)
        except UserLogin.DoesNotExist:
            print(f"User not found: {user_id}")
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except Exception as e:
            print(f"Error in get_profile: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def update_payment_status(request):
    """Update payment status after successful payment"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            payment_status = data.get('payment_status', True)
            
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'User ID is required'
                }, status=400)
            
            payment_method = data.get('payment_method', '')
            
            user = UserLogin.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            profile.payment_status = payment_status
            if payment_method:
                profile.payment_method = payment_method
            profile.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Payment status updated successfully',
                'payment_status': profile.payment_status
            }, status=200)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Profile not found'
            }, status=404)
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
def get_trainer_users(request, trainer_id):
    """Get all users assigned to a specific trainer (only paid users)"""
    if request.method == 'GET':
        try:
            trainer = Trainer.objects.get(id=trainer_id)
            profiles = UserProfile.objects.filter(
                assigned_trainer=trainer,
                payment_status=True  # Only show paid users
            ).select_related('user').order_by('-created_at')
            
            user_list = []
            for profile in profiles:
                user = profile.user
                
                # Calculate remaining days
                remaining_days = profile.get_remaining_days()
                
                # Get attendance stats
                total_attendance = Attendance.objects.filter(
                    user=user,
                    trainer=trainer,
                    status='accepted'
                ).count()
                
                pending_attendance = Attendance.objects.filter(
                    user=user,
                    trainer=trainer,
                    status='pending'
                ).count()
                
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.emailid,
                    'mobile': profile.mobile_number,
                    'age': profile.age,
                    'gender': profile.gender,
                    'current_weight': profile.current_weight,
                    'current_height': profile.current_height,
                    'goal': profile.goal,
                    'target_weight': profile.target_weight,
                    'target_months': profile.target_months,
                    'remaining_days': remaining_days,
                    'workout_time': profile.workout_time,
                    'diet_preference': profile.diet_preference,
                    'food_allergies': profile.food_allergies or '',
                    'health_conditions': profile.health_conditions or '',
                    'payment_amount': profile.payment_amount,
                    'total_attendance': total_attendance,
                    'pending_attendance': pending_attendance,
                    'created_at': profile.created_at.strftime('%Y-%m-%d')
                }
                user_list.append(user_data)
            
            return JsonResponse({
                'success': True,
                'users': user_list,
                'total': len(user_list)
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
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def request_attendance(request):
    """User requests attendance for today"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'User ID is required'
                }, status=400)
            
            user = UserLogin.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            
            if not profile.assigned_trainer:
                return JsonResponse({
                    'success': False,
                    'message': 'No trainer assigned to this user'
                }, status=400)
            
            # Check if attendance already requested for today
            today = datetime.now().date()
            if Attendance.objects.filter(user=user, date=today).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Attendance already requested for today'
                }, status=400)
            
            # Create attendance request
            attendance = Attendance.objects.create(
                user=user,
                trainer=profile.assigned_trainer,
                date=today,
                status='pending'
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Attendance request submitted successfully',
                'attendance': {
                    'id': attendance.id,
                    'date': attendance.date.strftime('%Y-%m-%d'),
                    'status': attendance.status
                }
            }, status=201)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User profile not found'
            }, status=404)
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
def get_user_attendance(request, user_id):
    """Get attendance history for a specific user"""
    if request.method == 'GET':
        try:
            user = UserLogin.objects.get(id=user_id)
            attendances = Attendance.objects.filter(user=user).order_by('-date')
            
            attendance_list = []
            for att in attendances:
                attendance_list.append({
                    'id': att.id,
                    'date': att.date.strftime('%Y-%m-%d'),
                    'status': att.status,
                    'request_date': att.request_date.strftime('%Y-%m-%d %H:%M'),
                    'accepted_date': att.accepted_date.strftime('%Y-%m-%d %H:%M') if att.accepted_date else None
                })
            
            total_accepted = attendances.filter(status='accepted').count()
            total_pending = attendances.filter(status='pending').count()
            
            return JsonResponse({
                'success': True,
                'attendances': attendance_list,
                'total_accepted': total_accepted,
                'total_pending': total_pending
            }, status=200)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
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
def accept_attendance(request):
    """Trainer accepts user's attendance request"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            attendance_id = data.get('attendance_id')
            status = data.get('status', 'accepted')  # accepted or rejected
            
            if not attendance_id:
                return JsonResponse({
                    'success': False,
                    'message': 'Attendance ID is required'
                }, status=400)
            
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.status = status
            if status == 'accepted':
                attendance.accepted_date = datetime.now()
            attendance.save()
            
            return JsonResponse({
                'success': True,
                'message': f'Attendance {status} successfully',
                'attendance': {
                    'id': attendance.id,
                    'user': attendance.user.name,
                    'date': attendance.date.strftime('%Y-%m-%d'),
                    'status': attendance.status
                }
            }, status=200)
            
        except Attendance.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Attendance record not found'
            }, status=404)
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
def get_pending_attendance_requests(request, trainer_id):
    """Get all pending attendance requests for a trainer"""
    if request.method == 'GET':
        try:
            trainer = Trainer.objects.get(id=trainer_id)
            pending_requests = Attendance.objects.filter(
                trainer=trainer,
                status='pending'
            ).select_related('user').order_by('-date')
            
            request_list = []
            for att in pending_requests:
                request_list.append({
                    'id': att.id,
                    'user_id': att.user.id,
                    'user_name': att.user.name,
                    'date': att.date.strftime('%Y-%m-%d'),
                    'request_date': att.request_date.strftime('%Y-%m-%d %H:%M')
                })
            
            return JsonResponse({
                'success': True,
                'requests': request_list,
                'total': len(request_list)
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
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def create_review(request):
    """User creates a review for their trainer (once per month)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            rating = data.get('rating')
            review_text = data.get('review_text')
            
            if not all([user_id, rating, review_text]):
                return JsonResponse({
                    'success': False,
                    'message': 'User ID, rating, and review text are required'
                }, status=400)
            
            if rating not in [1, 2, 3, 4, 5]:
                return JsonResponse({
                    'success': False,
                    'message': 'Rating must be between 1 and 5'
                }, status=400)
            
            user = UserLogin.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            
            if not profile.assigned_trainer:
                return JsonResponse({
                    'success': False,
                    'message': 'No trainer assigned to this user'
                }, status=400)
            
            # Check if user already posted review this month
            from django.utils import timezone
            one_month_ago = timezone.now() - relativedelta(months=1)
            recent_review = Review.objects.filter(
                user=user,
                trainer=profile.assigned_trainer,
                created_at__gte=one_month_ago
            ).first()
            
            if recent_review:
                return JsonResponse({
                    'success': False,
                    'message': 'You can only post one review per month. Try again later.'
                }, status=400)
            
            # Create review
            review = Review.objects.create(
                user=user,
                trainer=profile.assigned_trainer,
                rating=rating,
                review_text=review_text
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Review posted successfully',
                'review': {
                    'id': review.id,
                    'rating': review.rating,
                    'review_text': review.review_text,
                    'created_at': review.created_at.strftime('%Y-%m-%d %H:%M')
                }
            }, status=201)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User profile not found'
            }, status=404)
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
def get_trainer_reviews(request, trainer_id):
    """Get all reviews for a specific trainer"""
    if request.method == 'GET':
        try:
            trainer = Trainer.objects.get(id=trainer_id)
            reviews = Review.objects.filter(trainer=trainer).select_related('user').order_by('-created_at')
            
            review_list = []
            total_rating = 0
            
            for review in reviews:
                review_list.append({
                    'id': review.id,
                    'user_name': review.user.name,
                    'rating': review.rating,
                    'review_text': review.review_text,
                    'created_at': review.created_at.strftime('%Y-%m-%d'),
                    'time': review.created_at.strftime('%H:%M')
                })
                total_rating += review.rating
            
            average_rating = round(total_rating / len(reviews), 1) if reviews.exists() else 0
            
            return JsonResponse({
                'success': True,
                'reviews': review_list,
                'total_reviews': len(review_list),
                'average_rating': average_rating
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
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def get_all_reviews(request):
    """Get all reviews from all users (for admin)"""
    if request.method == 'GET':
        try:
            reviews = Review.objects.select_related('user', 'trainer__user').order_by('-created_at')
            
            review_list = []
            for review in reviews:
                review_list.append({
                    'id': review.id,
                    'user_name': review.user.name,
                    'user_email': review.user.emailid,
                    'trainer_name': review.trainer.user.name,
                    'rating': review.rating,
                    'review_text': review.review_text,
                    'created_at': review.created_at.strftime('%Y-%m-%d %H:%M')
                })
            
            return JsonResponse({
                'success': True,
                'reviews': review_list,
                'total': len(review_list)
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


# ==================== DIET PLAN APIs ====================

@csrf_exempt
def get_food_items(request):
    """Get all food items, optionally filtered by user allergies"""
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            exclude_allergies = request.GET.get('exclude_allergies', 'false').lower() == 'true'
            
            foods = FoodItem.objects.all()
            
            # Filter by user's diet preference and allergies
            if user_id and exclude_allergies:
                try:
                    user = UserLogin.objects.get(id=user_id)
                    profile = UserProfile.objects.get(user=user)
                    
                    # Filter by diet preference
                    # vegan: only vegan foods
                    # vegetarian: vegan + vegetarian foods (no meat/seafood)
                    # non_veg: all foods
                    if profile.diet_preference == 'vegan':
                        foods = foods.filter(diet_type='vegan')
                    elif profile.diet_preference == 'vegetarian':
                        foods = foods.filter(diet_type__in=['vegan', 'vegetarian'])
                    # non_veg gets all foods (no filter needed)
                    
                    # Filter out allergic foods
                    if profile.food_allergies:
                        allergies = [a.strip().lower() for a in profile.food_allergies.split(',')]
                        # Map common allergy terms to food categories
                        allergy_category_map = {
                            'milk': 'dairy',
                            'dairy': 'dairy',
                            'seafood': 'seafood',
                            'fish': 'seafood',
                            'nuts': 'nuts',
                            'eggs': 'eggs',
                            'egg': 'eggs'
                        }
                        
                        excluded_categories = []
                        for allergy in allergies:
                            if allergy in allergy_category_map:
                                excluded_categories.append(allergy_category_map[allergy])
                        
                        if excluded_categories:
                            foods = foods.exclude(food_category__in=excluded_categories)
                except:
                    pass  # If user not found, return all foods
            
            food_list = []
            for food in foods:
                food_list.append({
                    'id': food.id,
                    'name': food.name,
                    'category': food.food_category,
                    'diet_type': food.diet_type,
                    'calories': float(food.calories),
                    'protein': float(food.protein),
                    'carbs': float(food.carbs),
                    'fats': float(food.fats),
                    'serving_size': food.serving_size
                })
            
            return JsonResponse({
                'success': True,
                'foods': food_list,
                'total': len(food_list)
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
def get_diet_templates(request):
    """Get diet plan templates filtered by goal and calorie range"""
    if request.method == 'GET':
        try:
            goal = request.GET.get('goal')  # weight_loss, weight_gain, muscle_building
            target_calories = request.GET.get('target_calories')
            
            templates = DietPlanTemplate.objects.all()
            
            if goal:
                templates = templates.filter(goal_type=goal)
            
            if target_calories:
                cal = int(target_calories)
                templates = templates.filter(calorie_min__lte=cal, calorie_max__gte=cal)
            
            template_list = []
            for template in templates:
                template_list.append({
                    'id': template.id,
                    'name': template.name,
                    'goal_type': template.goal_type,
                    'calorie_min': template.calorie_min,
                    'calorie_max': template.calorie_max,
                    'description': template.description,
                    'meals_data': template.meals_data
                })
            
            return JsonResponse({
                'success': True,
                'templates': template_list,
                'total': len(template_list)
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
def calculate_target_calories(request, user_id):
    """Calculate recommended daily calories based on user's goal"""
    if request.method == 'GET':
        try:
            user = UserLogin.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            
            current_weight = float(profile.current_weight)
            goal = profile.goal
            
            # Calculate base calories
            if goal == 'weight_loss':
                target_calories = int(current_weight * 24 - 500)
            elif goal == 'weight_gain':
                target_calories = int(current_weight * 24 + 500)
            elif goal == 'muscle_building':
                target_calories = int(current_weight * 30)
            else:
                target_calories = int(current_weight * 24)
            
            # Ensure minimum healthy calories
            target_calories = max(target_calories, 1200)
            
            return JsonResponse({
                'success': True,
                'user_id': user_id,
                'goal': goal,
                'current_weight': current_weight,
                'target_calories': target_calories,
                'food_allergies': profile.food_allergies if profile.food_allergies else 'none',
                'diet_preference': profile.diet_preference
            }, status=200)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User profile not found'
            }, status=404)
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
def create_user_diet_plan(request):
    """Trainer creates a personalized diet plan for a user"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            trainer_id = data.get('trainer_id')
            template_id = data.get('template_id')
            plan_name = data.get('plan_name')
            target_calories = data.get('target_calories')
            meals_data = data.get('meals_data')
            notes = data.get('notes', '')
            start_date = data.get('start_date')
            
            if not all([user_id, trainer_id, plan_name, target_calories, meals_data]):
                return JsonResponse({
                    'success': False,
                    'message': 'Missing required fields'
                }, status=400)
            
            user = UserLogin.objects.get(id=user_id)
            trainer = Trainer.objects.get(id=trainer_id)
            template = DietPlanTemplate.objects.get(id=template_id) if template_id else None
            
            # Convert start_date string to date object if provided
            if start_date:
                if isinstance(start_date, str):
                    from datetime import datetime
                    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                else:
                    start_date_obj = start_date
            else:
                start_date_obj = date.today()
            
            # Deactivate existing active plans
            UserDietPlan.objects.filter(user=user, is_active=True).update(is_active=False)
            
            # Create new diet plan
            diet_plan = UserDietPlan.objects.create(
                user=user,
                trainer=trainer,
                template=template,
                plan_name=plan_name,
                target_calories=target_calories,
                meals_data=meals_data,
                notes=notes,
                start_date=start_date_obj,
                is_active=True
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Diet plan created successfully',
                'diet_plan': {
                    'id': diet_plan.id,
                    'plan_name': diet_plan.plan_name,
                    'target_calories': diet_plan.target_calories,
                    'start_date': diet_plan.start_date.strftime('%Y-%m-%d')
                }
            }, status=201)
            
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
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)


@csrf_exempt
def get_user_diet_plan(request, user_id):
    """Get active diet plan for a user"""
    if request.method == 'GET':
        try:
            user = UserLogin.objects.get(id=user_id)
            diet_plan = UserDietPlan.objects.filter(user=user, is_active=True).first()
            
            if not diet_plan:
                return JsonResponse({
                    'success': True,
                    'has_plan': False,
                    'message': 'No active diet plan found'
                }, status=200)
            
            return JsonResponse({
                'success': True,
                'has_plan': True,
                'diet_plan': {
                    'id': diet_plan.id,
                    'plan_name': diet_plan.plan_name,
                    'target_calories': diet_plan.target_calories,
                    'meals_data': diet_plan.meals_data,
                    'notes': diet_plan.notes,
                    'start_date': diet_plan.start_date.strftime('%Y-%m-%d'),
                    'trainer_name': diet_plan.trainer.user.name,
                    'created_at': diet_plan.created_at.strftime('%Y-%m-%d')
                }
            }, status=200)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
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
def get_trainer_diet_plans(request, trainer_id):
    """Get all diet plans created by a trainer"""
    if request.method == 'GET':
        try:
            trainer = Trainer.objects.get(id=trainer_id)
            diet_plans = UserDietPlan.objects.filter(trainer=trainer).select_related('user').order_by('-created_at')
            
            plan_list = []
            for plan in diet_plans:
                plan_list.append({
                    'id': plan.id,
                    'user_name': plan.user.name,
                    'user_id': plan.user.id,
                    'plan_name': plan.plan_name,
                    'target_calories': plan.target_calories,
                    'start_date': plan.start_date.strftime('%Y-%m-%d'),
                    'is_active': plan.is_active,
                    'created_at': plan.created_at.strftime('%Y-%m-%d')
                })
            
            return JsonResponse({
                'success': True,
                'diet_plans': plan_list,
                'total': len(plan_list)
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
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)
