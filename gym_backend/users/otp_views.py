import json
import random
import string
from datetime import timedelta
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import OTP, UserLogin


def _generate_otp():
    return ''.join(random.choices(string.digits, k=6))


@csrf_exempt
@require_http_methods(["POST"])
def send_otp(request):
    """Generate OTP and print in terminal (no email)."""
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()

        if not email or '@' not in email:
            return JsonResponse({'success': False, 'message': 'Please enter a valid email address'}, status=400)

        if UserLogin.objects.filter(emailid=email).exists():
            return JsonResponse({'success': False, 'message': 'This email is already registered. Please login instead.'}, status=400)

        OTP.objects.filter(email=email).delete()

        otp_code = _generate_otp()
        expires_at = timezone.now() + timedelta(minutes=10)
        otp = OTP.objects.create(email=email, otp_code=otp_code, expires_at=expires_at)

        print("\n" + "=" * 60)
        print(f"🔐 OTP Generated for: {email}")
        print(f"📝 OTP Code: {otp_code}")
        print(f"⏰ Expires at: {expires_at}")
        print("=" * 60 + "\n")

        return JsonResponse({'success': True, 'message': 'OTP generated. Check terminal.', 'otp_id': otp.id}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def verify_otp(request):
    """Verify OTP entered by user."""
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()
        otp_code = data.get('otp_code', '').strip()

        if not email or not otp_code:
            return JsonResponse({'success': False, 'message': 'Email and OTP are required'}, status=400)

        try:
            otp = OTP.objects.get(email=email)
        except OTP.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'No OTP found. Please request a new one.'}, status=400)

        if otp.is_verified:
            return JsonResponse({'success': False, 'message': 'OTP already verified'}, status=400)

        if otp.is_expired():
            otp.delete()
            return JsonResponse({'success': False, 'message': 'OTP has expired. Please request a new one.'}, status=400)

        if otp.attempt_count >= 5:
            otp.delete()
            return JsonResponse({'success': False, 'message': 'Too many attempts. Please request a new OTP.'}, status=400)

        if otp.otp_code != otp_code:
            otp.attempt_count += 1
            otp.save()
            return JsonResponse({'success': False, 'message': 'Invalid OTP'}, status=400)

        otp.is_verified = True
        otp.save()

        return JsonResponse({'success': True, 'message': 'OTP verified successfully', 'email': email}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def resend_otp(request):
    """Resend OTP (prints new OTP in terminal)."""
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()

        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required'}, status=400)

        try:
            otp = OTP.objects.get(email=email, is_verified=False)
        except OTP.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'No OTP found. Please request a new one.'}, status=400)

        if otp.attempt_count >= 3:
            otp.delete()
            return JsonResponse({'success': False, 'message': 'Max resend attempts exceeded. Please request new OTP.'}, status=400)

        otp.otp_code = _generate_otp()
        otp.expires_at = timezone.now() + timedelta(minutes=10)
        otp.attempt_count += 1
        otp.save()

        print("\n" + "=" * 60)
        print(f"🔐 OTP Resent for: {email}")
        print(f"📝 OTP Code: {otp.otp_code}")
        print(f"⏰ Expires at: {otp.expires_at}")
        print("=" * 60 + "\n")

        return JsonResponse({'success': True, 'message': 'OTP resent. Check terminal.'}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
