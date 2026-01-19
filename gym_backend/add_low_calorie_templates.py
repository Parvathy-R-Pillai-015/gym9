"""
Add low calorie templates for lighter users
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate

# Add lower calorie templates
templates = [
    {
        'name': 'Weight Gain - Low Calorie (1200-2000)',
        'goal_type': 'weight_gain',
        'calorie_min': 1200,
        'calorie_max': 2000,
        'description': 'Weight gain plan for lighter individuals',
        'meals_data': {
            'breakfast': [
                {'food': 'Oats', 'quantity': '50g', 'calories': 195},
                {'food': 'Banana', 'quantity': '1 medium', 'calories': 105},
                {'food': 'Almonds', 'quantity': '15g', 'calories': 87},
                {'food': 'Milk (whole)', 'quantity': '200ml', 'calories': 122}
            ],
            'lunch': [
                {'food': 'Rice (white, cooked)', 'quantity': '150g', 'calories': 195},
                {'food': 'Tofu', 'quantity': '150g', 'calories': 114},
                {'food': 'Chickpeas (cooked)', 'quantity': '100g', 'calories': 164},
                {'food': 'Mixed vegetables', 'quantity': '100g', 'calories': 50}
            ],
            'dinner': [
                {'food': 'Roti (wheat)', 'quantity': '3 pieces', 'calories': 213},
                {'food': 'Lentils (cooked)', 'quantity': '150g', 'calories': 174},
                {'food': 'Paneer', 'quantity': '50g', 'calories': 133}
            ],
            'snacks': [
                {'food': 'Banana', 'quantity': '1 piece', 'calories': 105},
                {'food': 'Peanuts', 'quantity': '15g', 'calories': 85},
                {'food': 'Apple', 'quantity': '1 medium', 'calories': 95}
            ]
        }
    },
    {
        'name': 'Weight Loss - Very Low Calorie (1000-1200)',
        'goal_type': 'weight_loss',
        'calorie_min': 1000,
        'calorie_max': 1200,
        'description': 'Very low calorie plan for rapid weight loss (medical supervision recommended)',
        'meals_data': {
            'breakfast': [
                {'food': 'Oats', 'quantity': '30g', 'calories': 117},
                {'food': 'Egg white', 'quantity': '2 pieces', 'calories': 104},
                {'food': 'Orange', 'quantity': '1 medium', 'calories': 62}
            ],
            'lunch': [
                {'food': 'Chicken breast', 'quantity': '100g', 'calories': 165},
                {'food': 'Broccoli', 'quantity': '100g', 'calories': 34},
                {'food': 'Spinach', 'quantity': '100g', 'calories': 23},
                {'food': 'Rice (brown, cooked)', 'quantity': '80g', 'calories': 89}
            ],
            'dinner': [
                {'food': 'Fish (tuna)', 'quantity': '100g', 'calories': 132},
                {'food': 'Mixed vegetables', 'quantity': '100g', 'calories': 50},
                {'food': 'Roti (wheat)', 'quantity': '1 piece', 'calories': 71}
            ],
            'snacks': [
                {'food': 'Apple', 'quantity': '1 medium', 'calories': 95},
                {'food': 'Carrot', 'quantity': '100g', 'calories': 41}
            ]
        }
    },
    {
        'name': 'Muscle Building - Low Calorie (1800-2200)',
        'goal_type': 'muscle_building',
        'calorie_min': 1800,
        'calorie_max': 2200,
        'description': 'High protein plan for lean muscle building',
        'meals_data': {
            'breakfast': [
                {'food': 'Egg (whole)', 'quantity': '3 pieces', 'calories': 465},
                {'food': 'Oats', 'quantity': '40g', 'calories': 156},
                {'food': 'Banana', 'quantity': '1 piece', 'calories': 105}
            ],
            'lunch': [
                {'food': 'Chicken breast', 'quantity': '150g', 'calories': 248},
                {'food': 'Quinoa', 'quantity': '100g', 'calories': 120},
                {'food': 'Broccoli', 'quantity': '100g', 'calories': 34},
                {'food': 'Sweet potato', 'quantity': '100g', 'calories': 86}
            ],
            'dinner': [
                {'food': 'Fish (tuna)', 'quantity': '150g', 'calories': 198},
                {'food': 'Rice (brown, cooked)', 'quantity': '150g', 'calories': 167},
                {'food': 'Tofu', 'quantity': '100g', 'calories': 76}
            ],
            'snacks': [
                {'food': 'Egg white', 'quantity': '3 pieces', 'calories': 156},
                {'food': 'Almonds', 'quantity': '20g', 'calories': 116},
                {'food': 'Apple', 'quantity': '1 piece', 'calories': 95}
            ]
        }
    }
]

created_count = 0
for template in templates:
    obj, created = DietPlanTemplate.objects.get_or_create(
        name=template['name'],
        defaults={
            'goal_type': template['goal_type'],
            'calorie_min': template['calorie_min'],
            'calorie_max': template['calorie_max'],
            'description': template['description'],
            'meals_data': template['meals_data']
        }
    )
    if created:
        created_count += 1
        print(f"✅ Created: {template['name']}")
    else:
        print(f"⏭️  Already exists: {template['name']}")

print(f"\n✅ Added {created_count} new templates")
print(f"📊 Total templates: {DietPlanTemplate.objects.count()}")
