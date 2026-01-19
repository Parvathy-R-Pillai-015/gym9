import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate
import json

# Delete old templates and create new 7-day templates
# We'll create simpler templates first - 3 main ones covering most cases

print("Creating 7-DAY MEAL PLAN TEMPLATES")
print("=" * 80)

# Clear existing templates
DietPlanTemplate.objects.all().delete()
print("✓ Cleared old templates")

# Template 1: Weight Loss (1500-2000 cal) - Vegetarian friendly
template1 = DietPlanTemplate.objects.create(
    name="Weight Loss - Balanced (1500-2000)",
    goal_type="weight_loss",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day balanced weight loss plan with variety",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "10g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Carrots", "quantity": "50g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Paneer", "quantity": "50g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Tomato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "10g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Mango", "quantity": "100g"}, {"food": "Peanuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "10g"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "10g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Quinoa", "quantity": "85g"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "10g"}]
        }
    }
)
print(f"✓ Created: {template1.name}")

# Template 2: Weight Gain (1800-2200 cal) - Vegan friendly
template2 = DietPlanTemplate.objects.create(
    name="Weight Gain - Plant Based (1800-2200)",
    goal_type="weight_gain",
    calorie_min=1800,
    calorie_max=2200,
    description="7-day vegan weight gain plan with high calories",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "100g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Peanuts", "quantity": "15g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "180g"}, {"food": "Tofu", "quantity": "150g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "150g"}, {"food": "Potato", "quantity": "120g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "25g"}, {"food": "Mango", "quantity": "100g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "20g"}],
            "lunch": [{"food": "Quinoa", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "160g"}, {"food": "Black beans", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "2 medium"}, {"food": "Peanuts", "quantity": "30g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "110g"}, {"food": "Mango", "quantity": "150g"}, {"food": "Almonds", "quantity": "25g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "150g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "180g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Walnuts", "quantity": "20g"}],
            "lunch": [{"food": "Quinoa", "quantity": "150g"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Tomato", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Black beans", "quantity": "150g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "100g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "22g"}, {"food": "Cashews", "quantity": "15g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "170g"}, {"food": "Tofu", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "150g"}, {"food": "Potato", "quantity": "120g"}],
            "snacks": [{"food": "Apple", "quantity": "2 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Sweet potato", "quantity": "120g"}, {"food": "Peanuts", "quantity": "25g"}],
            "lunch": [{"food": "Quinoa", "quantity": "140g"}, {"food": "Black beans", "quantity": "150g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "180g"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "25g"}, {"food": "Mango", "quantity": "100g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "110g"}, {"food": "Orange", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "25g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "150g"}, {"food": "Potato", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "170g"}, {"food": "Lentils (cooked)", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "2 medium"}, {"food": "Walnuts", "quantity": "22g"}, {"food": "Banana", "quantity": "1 medium"}]
        }
    }
)
print(f"✓ Created: {template2.name}")

# Template 3: Weight Gain (1800-2200 cal) - Non-Veg
template3 = DietPlanTemplate.objects.create(
    name="Weight Gain - Non-Veg (1800-2200)",
    goal_type="weight_gain",
    calorie_min=1800,
    calorie_max=2200,
    description="7-day non-vegetarian weight gain plan with chicken",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "180g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "170g"}, {"food": "Chicken thigh", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Mango", "quantity": "120g"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Mixed vegetables", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "180g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "170g"}, {"food": "Mutton", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "180g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Mango", "quantity": "100g"}],
            "lunch": [{"food": "Quinoa", "quantity": "140g"}, {"food": "Chicken thigh", "quantity": "150g"}, {"food": "Mixed vegetables", "quantity": "120g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "170g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Peanuts", "quantity": "20g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Mutton", "quantity": "130g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "180g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}]
        }
    }
)
print(f"✓ Created: {template3.name}")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
templates = DietPlanTemplate.objects.all()
for t in templates:
    print(f"  {t.name}")
    print(f"    Goal: {t.goal_type} | Calories: {t.calorie_min}-{t.calorie_max}")
    print(f"    Days: {len(t.meals_data)} days")
print(f"\nTotal templates: {templates.count()}")
