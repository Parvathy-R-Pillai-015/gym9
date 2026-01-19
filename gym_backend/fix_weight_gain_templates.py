import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate
import json

print("Creating PERSONALIZED Weight Gain Templates by Diet Type")
print("=" * 80)

# Delete the generic "Light Users" template and replace with diet-specific ones
DietPlanTemplate.objects.filter(name="Weight Gain - Light Users (1200-1800)").delete()
print("✓ Removed generic 'Light Users' template")

# Template 1: VEGAN Weight Gain (1200-1800) for Priya, Sherin
template_vegan = DietPlanTemplate.objects.create(
    name="Weight Gain - Vegan (1200-1800)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1800,
    description="7-day vegan weight gain plan with plant-based proteins",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Peanuts", "quantity": "15g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Mango", "quantity": "100g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "18g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Mango", "quantity": "120g"}, {"food": "Almonds", "quantity": "22g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "18g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Tomato", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Mango", "quantity": "100g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "22g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "20g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Black beans", "quantity": "130g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Peanuts", "quantity": "25g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "22g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print(f"✓ Created: {template_vegan.name}")

# Template 2: VEGETARIAN Weight Gain (1200-1800) for vegetarian users
template_veg = DietPlanTemplate.objects.create(
    name="Weight Gain - Vegetarian (1200-1800)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1800,
    description="7-day vegetarian weight gain with dairy and eggs",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Tomato", "quantity": "80g"}, {"food": "Broccoli", "quantity": "60g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Broccoli", "quantity": "80g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "18g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Spinach", "quantity": "60g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}]
        }
    }
)
print(f"✓ Created: {template_veg.name}")

# Template 3: NON-VEG Weight Gain (1200-1800) for dinju
template_nonveg = DietPlanTemplate.objects.create(
    name="Weight Gain - Non-Veg (1200-1800)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1800,
    description="7-day non-veg weight gain with chicken and eggs",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken thigh", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Broccoli", "quantity": "80g"}, {"food": "Tomato", "quantity": "60g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Chicken thigh", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Mutton", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Almonds", "quantity": "15g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Spinach", "quantity": "60g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Orange", "quantity": "1 medium"}]
        }
    }
)
print(f"✓ Created: {template_nonveg.name}")

print("\n" + "=" * 80)
print("UPDATED WEIGHT GAIN TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='weight_gain').order_by('calorie_min')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")
print(f"\nTotal weight_gain templates: {templates.count()}")
