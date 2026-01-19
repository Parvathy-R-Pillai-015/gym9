import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate

print("=" * 80)
print("CREATING MUSCLE_GAIN TEMPLATES")
print("=" * 80)

# Duplicate muscle_building templates as muscle_gain
muscle_templates = DietPlanTemplate.objects.filter(goal_type='muscle_building')
for t in muscle_templates:
    new_template = DietPlanTemplate.objects.create(
        name=t.name.replace('Muscle Building', 'Muscle Gain'),
        goal_type='muscle_gain',
        calorie_min=t.calorie_min,
        calorie_max=t.calorie_max,
        description=t.description.replace('muscle building', 'muscle gain'),
        meals_data=t.meals_data
    )
    print(f'✓ Created: {new_template.name}')

print(f'\nTotal muscle_gain templates: {DietPlanTemplate.objects.filter(goal_type="muscle_gain").count()}')
