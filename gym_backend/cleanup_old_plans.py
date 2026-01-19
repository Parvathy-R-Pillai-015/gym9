import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate, UserDietPlan

print("=" * 80)
print("CHECKING FOR OLD TEMPLATES AND DIET PLANS")
print("=" * 80)

# Check all templates
print("\nALL TEMPLATES IN DATABASE:")
all_templates = DietPlanTemplate.objects.all().order_by('goal_type', 'calorie_min')
for t in all_templates:
    meals_format = "7-DAY" if isinstance(t.meals_data, dict) and 'monday' in t.meals_data else "1-DAY"
    print(f"  [{meals_format}] {t.calorie_min:4d}-{t.calorie_max:4d} | {t.goal_type:15s} | {t.name}")

# Check existing diet plans for users
print("\n" + "=" * 80)
print("EXISTING USER DIET PLANS:")
print("=" * 80)
plans = UserDietPlan.objects.all()
for plan in plans:
    meals_format = "7-DAY" if isinstance(plan.meals_data, dict) and 'monday' in plan.meals_data else "1-DAY"
    template_name = plan.template.name if plan.template else plan.plan_name
    print(f"  [{meals_format}] {plan.user.name:15s} | {template_name} | Created: {plan.created_at.strftime('%Y-%m-%d')}")

# Delete old diet plans with 1-day format
print("\n" + "=" * 80)
print("DELETING OLD 1-DAY DIET PLANS:")
print("=" * 80)
deleted_count = 0
for plan in plans:
    if not (isinstance(plan.meals_data, dict) and 'monday' in plan.meals_data):
        template_name = plan.template.name if plan.template else plan.plan_name
        print(f"  ✗ Deleting old plan for {plan.user.name}: {template_name}")
        plan.delete()
        deleted_count += 1

print(f"\nDeleted {deleted_count} old diet plans")
print("\nUsers need to create NEW diet plans with updated templates!")
