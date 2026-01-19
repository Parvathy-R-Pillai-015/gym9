import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate
import json

print("Adding MORE TEMPLATES to cover all calorie ranges")
print("=" * 80)

# Add more weight_gain templates for lower calorie ranges (1200-1800)
template_low_gain = DietPlanTemplate.objects.create(
    name="Weight Gain - Light Users (1200-1800)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1800,
    description="7-day weight gain plan for lighter individuals",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "150ml"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Tomato", "quantity": "80g"}, {"food": "Broccoli", "quantity": "60g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "150ml"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Spinach", "quantity": "60g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        }
    }
)
print(f"✓ Created: {template_low_gain.name} ({template_low_gain.calorie_min}-{template_low_gain.calorie_max})")

# Add weight_loss template for higher calories (2000-2500)
template_high_loss = DietPlanTemplate.objects.create(
    name="Weight Loss - High Calorie (2000-2500)",
    goal_type="weight_loss",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day weight loss plan for heavier individuals",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}, {"food": "Tomato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "22g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "100g"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "2 medium"}, {"food": "Walnuts", "quantity": "20g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "150g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Almonds", "quantity": "22g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}]
        }
    }
)
print(f"✓ Created: {template_high_loss.name} ({template_high_loss.calorie_min}-{template_high_loss.calorie_max})")

# Add muscle building template for lower range (1500-2000)
template_muscle_low = DietPlanTemplate.objects.create(
    name="Muscle Building - Moderate (1500-2000)",
    goal_type="muscle_building",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day muscle building plan with high protein",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Greek yogurt", "quantity": "100g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Milk (whole)", "quantity": "200ml"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Walnuts", "quantity": "15g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Paneer", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Greek yogurt", "quantity": "100g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "22g"}, {"food": "Milk (whole)", "quantity": "200ml"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Greek yogurt", "quantity": "100g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "200ml"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Greek yogurt", "quantity": "100g"}]
        }
    }
)
print(f"✓ Created: {template_muscle_low.name} ({template_muscle_low.calorie_min}-{template_muscle_low.calorie_max})")

print("\n" + "=" * 80)
print("COMPLETE TEMPLATE LIST:")
print("=" * 80)
templates = DietPlanTemplate.objects.all().order_by('goal_type', 'calorie_min')
for t in templates:
    print(f"{t.goal_type.upper():20s} | {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")

print(f"\nTotal: {templates.count()} templates")
