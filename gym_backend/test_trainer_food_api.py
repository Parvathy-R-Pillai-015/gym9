#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import FoodEntry, UserLogin, Trainer, UserProfile
from datetime import datetime

# Test the data
trainer_id = 1
user_id = 23
target_date_str = '2026-01-26'

try:
    trainer = Trainer.objects.get(id=trainer_id)
    user = UserLogin.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user, assigned_trainer=trainer)
    
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
    entries = FoodEntry.objects.filter(
        user=user,
        entry_date=target_date
    )
    
    print(f"Trainer: {trainer}")
    print(f"User: {user}")
    print(f"Profile: {profile}")
    print(f"Target date: {target_date}")
    print(f"Entries count: {entries.count()}")
    
    for entry in entries:
        print(f"  Entry: {entry.id} - {entry.food_item.name if entry.food_item else 'No food_item'} - {entry.calculated_calories}")
        print(f"    Food item: {entry.food_item}")
        print(f"    Meal type: {entry.meal_type}")
        
except Exception as e:
    import traceback
    print(f"Error: {str(e)}")
    traceback.print_exc()
