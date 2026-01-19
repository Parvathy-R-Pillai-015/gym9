import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserLogin, UserProfile, UserDietPlan

print("Users with profiles and goals:")
print("-" * 70)
users = UserLogin.objects.filter(role='user')
for u in users:
    try:
        profile = UserProfile.objects.get(user=u)
        print(f"ID: {u.id} | Name: {u.name} | Weight: {profile.current_weight}kg | Goal: {profile.goal}")
    except UserProfile.DoesNotExist:
        print(f"ID: {u.id} | Name: {u.name} | No profile")

print("\nDiet Plans assigned:")
print("-" * 70)
plans = UserDietPlan.objects.all().select_related('user', 'template').order_by('-id')
for p in plans[:10]:
    try:
        user_profile = UserProfile.objects.get(user=p.user)
        user_goal = user_profile.goal
    except UserProfile.DoesNotExist:
        user_goal = 'N/A'
    template_goal = p.template.goal_type if p.template else 'N/A'
    print(f"User: {p.user.name} (Goal: {user_goal}) | Plan: {p.plan_name} | Target: {p.target_calories} cal | Template Goal: {template_goal}")
