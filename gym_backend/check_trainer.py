import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import Trainer, UserProfile

# Find trainer sooraj
trainer = Trainer.objects.filter(user__emailid='sooraj@gmail.com').first()

if trainer:
    print(f'Trainer ID: {trainer.id}')
    print(f'Trainer Name: {trainer.user.name}')
    print(f'Trainer Email: {trainer.user.emailid}')
    
    # Check assigned users
    profiles = UserProfile.objects.filter(assigned_trainer=trainer)
    print(f'\nAssigned Users: {profiles.count()}')
    
    for profile in profiles:
        print(f'\n  User: {profile.user.name}')
        print(f'  Email: {profile.user.emailid}')
        print(f'  Payment Status: {profile.payment_status}')
        print(f'  Goal: {profile.goal}')
else:
    print('Trainer sooraj@gmail.com not found')

# Also check all trainers
print('\n\nAll Trainers:')
for t in Trainer.objects.all():
    print(f'  - {t.user.name} ({t.user.emailid}) - ID: {t.id}')
