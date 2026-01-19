import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile

# Get weight gain users
users = UserProfile.objects.filter(goal='weight_gain').order_by('current_weight')
print('ACTUAL Backend Calculation (weight * 24 + 500):')
print('=' * 70)
for user in users:
    # This is what your backend ACTUALLY calculates:
    target = int(user.current_weight * 24 + 500)
    target = max(target, 1200)  # Minimum 1200 cal
    
    print(f'{user.user.name:16} | {user.current_weight:3.0f}kg | Target: {target:4d} cal | Diet: {user.diet_preference}')

print('\n' + '=' * 70)
print('CORRECT Template Ranges Needed:')
print('  dinju (20kg):    980 → 1200 cal (min enforced)')
print('  Sherin (42kg):  1508 cal')
print('  Aiswarya (50kg): 1700 cal')  
print('  Priya (51kg):   1724 cal')
print('\nSuggested Ranges:')
print('  1200-1500 cal → Light users (dinju)')
print('  1500-1800 cal → Medium users (Sherin, Aiswarya, Priya)')
print('  1800-2200 cal → Heavy users')
