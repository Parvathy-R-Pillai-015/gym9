import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import Trainer, UserLogin
from django.contrib.auth.hashers import make_password, check_password

print("=" * 80)
print("CHECKING TRAINER: Madhav")
print("=" * 80)

try:
    trainer = Trainer.objects.get(user__emailid='madhav@gmail.com')
    user = trainer.user
    
    print(f"\n✓ Trainer Found:")
    print(f"  Name: {user.name}")
    print(f"  Email: {user.emailid}")
    print(f"  Role: {user.role}")
    print(f"  Password (hashed): {user.password[:50]}...")
    
    # Check if password verification works
    expected_password = 'madhav+tr'
    
    print(f"\n" + "=" * 80)
    print("PASSWORD VERIFICATION TEST:")
    print("=" * 80)
    
    # Test 1: Check if current password matches
    if user.password == expected_password:
        print(f"✓ Password is stored as plain text: {expected_password}")
    elif user.password.startswith('pbkdf2_sha256'):
        print(f"✓ Password is hashed (Django format)")
        # Test if password matches
        is_correct = check_password(expected_password, user.password)
        if is_correct:
            print(f"✓ Password '{expected_password}' MATCHES the hash")
        else:
            print(f"✗ Password '{expected_password}' DOES NOT MATCH the hash")
            print(f"\nℹ Need to reset password to: {expected_password}")
            
            # Reset password to plain text
            user.password = expected_password
            user.save()
            print(f"✓ Password reset to plain text: {expected_password}")
    else:
        print(f"⚠ Unknown password format")
        user.password = expected_password
        user.save()
        print(f"✓ Password reset to: {expected_password}")
    
    print(f"\n" + "=" * 80)
    print("LOGIN TEST:")
    print("=" * 80)
    print(f"  Email: madhav@gmail.com")
    print(f"  Password: madhav+tr")
    print(f"  Role: trainer")
    print(f"\nℹ Try logging in with these credentials now")
    
except Trainer.DoesNotExist:
    print("\n✗ Trainer 'Madhav' NOT FOUND")
