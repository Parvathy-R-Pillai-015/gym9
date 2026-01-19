import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import Trainer

print("=" * 80)
print("CHECKING TRAINER: mahadev")
print("=" * 80)

# Search for trainer with email mahadev@gmail.com
try:
    trainer = Trainer.objects.get(user__emailid='mahadev@gmail.com')
    print(f"\n✓ Trainer Found:")
    print(f"  Name: {trainer.user.name}")
    print(f"  Email: {trainer.user.emailid}")
    print(f"  Password: {trainer.user.password}")
    print(f"  Role: {trainer.user.role}")
    print(f"  Experience: {trainer.experience} years")
    print(f"  Specialization: {trainer.specialization}")
    
    # Check if password needs update
    if trainer.user.password != 'mahadev+tr':
        print(f"\n⚠ Password mismatch!")
        print(f"  Current password in DB: {trainer.user.password}")
        print(f"  Expected password: mahadev+tr")
        
        # Update password
        trainer.user.password = 'mahadev+tr'
        trainer.user.save()
        print(f"\n✓ Password updated to: mahadev+tr")
    else:
        print(f"\n✓ Password is correct: mahadev+tr")
        
except Trainer.DoesNotExist:
    print("\n✗ Trainer with email 'mahadev@gmail.com' NOT FOUND")
    print("\nSearching for similar trainers:")
    trainers = Trainer.objects.all()
    for t in trainers:
        if 'mahadev' in t.user.name.lower() or 'mahadev' in t.user.emailid.lower():
            print(f"  - {t.user.name} ({t.user.emailid})")
    
    print("\n" + "=" * 80)
    print("ALL TRAINERS IN DATABASE:")
    print("=" * 80)
    for t in Trainer.objects.all():
        print(f"  {t.user.name:15} | {t.user.emailid:25} | Password: {t.user.password}")
