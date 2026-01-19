import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile

print("=" * 80)
print("CHECKING UNPAID USERS WITH TRAINER ASSIGNMENTS")
print("=" * 80)

# Find unpaid users with assigned trainers
unpaid_with_trainers = UserProfile.objects.filter(
    payment_status=False,  # False = unpaid
    assigned_trainer__isnull=False
)

print(f"\nFound {unpaid_with_trainers.count()} unpaid users with trainers assigned:")
print("-" * 80)
for profile in unpaid_with_trainers:
    print(f"  User: {profile.user.name:15s} | Email: {profile.user.emailid:25s} | Trainer: {profile.assigned_trainer.user.name}")
    
# Remove trainer assignments from unpaid users
if unpaid_with_trainers.count() > 0:
    print("\n" + "=" * 80)
    print("REMOVING TRAINER ASSIGNMENTS FROM UNPAID USERS")
    print("=" * 80)
    
    for profile in unpaid_with_trainers:
        print(f"  ✗ Removing trainer from {profile.user.name}")
        profile.assigned_trainer = None
        profile.save()
    
    print(f"\n✓ Removed trainer assignments from {unpaid_with_trainers.count()} unpaid users")
else:
    print("\n✓ No unpaid users have trainer assignments")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
print(f"Paid users with trainers: {UserProfile.objects.filter(payment_status=True, assigned_trainer__isnull=False).count()}")
print(f"Unpaid users with trainers: {UserProfile.objects.filter(payment_status=False, assigned_trainer__isnull=False).count()}")
