import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate, FoodItem
import json

# Create higher calorie weight loss templates for heavier users

template1 = DietPlanTemplate.objects.create(
    name="Weight Loss - High Calorie (1800-2200)",
    goal_type="weight_loss",
    calorie_min=1800,
    calorie_max=2200,
    description="Weight loss plan for heavier individuals",
    meals_data={
        "breakfast": [
            {"food": "Oats", "quantity": "80g"},
            {"food": "Banana", "quantity": "1 medium"},
            {"food": "Almonds", "quantity": "15g"},
            {"food": "Milk (whole)", "quantity": "200ml"}
        ],
        "lunch": [
            {"food": "Rice (white, cooked)", "quantity": "120g"},
            {"food": "Chicken breast", "quantity": "120g"},
            {"food": "Mixed vegetables", "quantity": "100g"},
            {"food": "Olive oil", "quantity": "5g"}
        ],
        "dinner": [
            {"food": "Roti (wheat)", "quantity": "2 pieces"},
            {"food": "Tofu", "quantity": "100g"},
            {"food": "Mixed vegetables", "quantity": "100g"},
            {"food": "Lentils (cooked)", "quantity": "100g"}
        ],
        "snacks": [
            {"food": "Apple", "quantity": "1 medium"},
            {"food": "Peanuts", "quantity": "20g"},
            {"food": "Greek yogurt", "quantity": "100g"}
        ]
    }
)

template2 = DietPlanTemplate.objects.create(
    name="Weight Loss - Very High Calorie (2200-2500)",
    goal_type="weight_loss",
    calorie_min=2200,
    calorie_max=2500,
    description="Weight loss plan for very heavy individuals or active users",
    meals_data={
        "breakfast": [
            {"food": "Oats", "quantity": "100g"},
            {"food": "Banana", "quantity": "2 medium"},
            {"food": "Walnuts", "quantity": "20g"},
            {"food": "Milk (whole)", "quantity": "250ml"},
            {"food": "Honey", "quantity": "15g"}
        ],
        "lunch": [
            {"food": "Rice (white, cooked)", "quantity": "150g"},
            {"food": "Chicken breast", "quantity": "150g"},
            {"food": "Mixed vegetables", "quantity": "150g"},
            {"food": "Paneer", "quantity": "50g"},
            {"food": "Olive oil", "quantity": "10g"}
        ],
        "dinner": [
            {"food": "Roti (wheat)", "quantity": "3 pieces"},
            {"food": "Tofu", "quantity": "120g"},
            {"food": "Mixed vegetables", "quantity": "120g"},
            {"food": "Lentils (cooked)", "quantity": "120g"},
            {"food": "Olive oil", "quantity": "5g"}
        ],
        "snacks": [
            {"food": "Apple", "quantity": "1 medium"},
            {"food": "Banana", "quantity": "1 medium"},
            {"food": "Peanuts", "quantity": "25g"},
            {"food": "Greek yogurt", "quantity": "150g"}
        ]
    }
)

print(f"Created: {template1.name} ({template1.calorie_min}-{template1.calorie_max} cal)")
print(f"Created: {template2.name} ({template2.calorie_min}-{template2.calorie_max} cal)")

# Show all weight_loss templates now
print("\nAll Weight Loss Templates:")
print("-" * 70)
templates = DietPlanTemplate.objects.filter(goal_type="weight_loss").order_by('calorie_min')
for t in templates:
    print(f"  {t.name}: {t.calorie_min}-{t.calorie_max} cal")
