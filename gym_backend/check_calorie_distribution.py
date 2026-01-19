import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile

# Get weight gain users
users = UserProfile.objects.filter(goal='weight_gain').order_by('current_weight')
print('Weight Gain Users Calorie Distribution:')
print('=' * 60)
for user in users:
    # Calculate TDEE (male formula)
    tdee = (10 * user.current_weight + 6.25 * user.current_height - 5 * user.age + 5) * 1.375
    # Add 300 for weight gain
    target = tdee + 300
    print(f'{user.user.name:12} | {user.current_weight:3.0f}kg | Target: {target:4.0f} cal | Diet: {user.diet_preference}')

print('\n' + '=' * 60)
print('Current Range: 1200-1800 cal (600 cal difference!)')
print('\nSuggested Better Ranges:')
print('  1200-1500 cal → Low range (dinju)')
print('  1500-1800 cal → Medium range (Sherin, Aiswarya, Priya)')
print('  1800-2200 cal → High range')
