import random
import string
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OTP, UserLogin

@csrf_exempt
@require_http_methods(["POST"])
def send_otp(request):
    """
    Generate OTP and print to terminal (development mode)
    No email sending required
    """
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()
        
        # Validate email format
        if not email or '@' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address'
            }, status=400)
        
        # Check if user already exists
        if UserLogin.objects.filter(emailid=email).exists():
            return JsonResponse({
                'success': False,
                'message': 'This email is already registered. Please login instead.'
            }, status=400)
        
        # Delete any previous OTP for this email (auto-cleanup)
        OTP.objects.filter(email=email).delete()
        
        # Generate 6-digit OTP
        otp_code = ''.join(random.choices(string.digits, k=6))
        
        # Create OTP record with 10-minute expiration
        expires_at = timezone.now() + timedelta(minutes=10)
        otp = OTP.objects.create(
            email=email,
            otp_code=otp_code,
            expires_at=expires_at
        )
        
        # Print OTP to terminal (development mode - no email sending)
        print("\n" + "="*60)
        print(f"🔐 OTP Generated for: {email}")
        print(f"📝 OTP Code: {otp_code}")
        print(f"⏰ Expires at: {expires_at}")
        print("="*60 + "\n")
        
        return JsonResponse({
            'success': True,
            'message': 'OTP generated successfully. Check terminal for code.',
            'otp_id': otp.id
        }, status=200)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def verify_otp(request):
    """
    Verify OTP entered by user
    """
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()
        otp_code = data.get('otp_code', '').strip()
        
        if not email or not otp_code:
            return JsonResponse({
                'success': False,
                'message': 'Email and OTP are required'
            }, status=400)
        
        # Check if OTP exists
        try:
            otp = OTP.objects.get(email=email, otp_code=otp_code)
        except OTP.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Invalid OTP'
            }, status=400)
        
        # Check if already verified
        if otp.is_verified:
            return JsonResponse({
                'success': False,
                'message': 'OTP already verified'
            }, status=400)
        
        # Check if expired
        if otp.is_expired():
            otp.delete()
            return JsonResponse({
                'success': False,
                'message': 'OTP has expired. Please request a new one.'
            }, status=400)
        
        # Check attempt count
        if otp.attempt_count >= 5:
            otp.delete()
            return JsonResponse({
                'success': False,
                'message': 'Too many failed attempts. Please request a new OTP.'
            }, status=400)
        
        # Mark as verified
        otp.is_verified = True
        otp.save()
        
        return JsonResponse({
            'success': True,
            'message': 'OTP verified successfully',
            'email': email
        }, status=200)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def resend_otp(request):
    """
    Resend OTP to email (max 3 times)
    """
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()
        
        if not email:
            return JsonResponse({
                'success': False,
                'message': 'Email is required'
            }, status=400)
        
        # Get existing OTP
        try:
            otp = OTP.objects.get(email=email, is_verified=False)
        except OTP.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'No OTP found for this email'
            }, status=400)
        
        # Check resend limit (using attempt_count as resend counter)
        if otp.attempt_count >= 3:
            otp.delete()
            return JsonResponse({
                'success': False,
                'message': 'Maximum resend attempts exceeded. Please request a new OTP.'
            }, status=400)
        
        # Try to send email again
        try:
            subject = 'Your Fitness Gym Registration OTP (Resend)'
            message = f"""
Hello,

Your OTP for Fitness Gym registration is: {otp.otp_code}

This OTP will expire in 10 minutes.

If you didn't request this OTP, please ignore this email.

Best regards,
Fitness Gym Team
            """
            
            send_mail(
                subject,
                message,
                'noreply@fitnessgym.com',
                [email],
                fail_silently=False,
            )
            
            # Increment resend attempt count
            otp.attempt_count += 1
            otp.save()
            
            return JsonResponse({
                'success': True,
                'message': 'OTP resent successfully',
                'attempts_remaining': 3 - otp.attempt_count
            }, status=200)
        
        except Exception as email_error:
            otp.delete()
            return JsonResponse({
                'success': False,
                'message': f'Failed to resend OTP: {str(email_error)}'
            }, status=400)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        }, status=500)
