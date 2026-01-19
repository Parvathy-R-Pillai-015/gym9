import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate
import json

print("Splitting Weight Gain Templates into Proper Calorie Ranges")
print("=" * 80)

# Delete old 1200-1800 templates (too wide!)
deleted = DietPlanTemplate.objects.filter(
    goal_type='weight_gain',
    calorie_min=1200,
    calorie_max=1800
).delete()
print(f"✓ Deleted {deleted[0]} old 1200-1800 templates (range too wide)")

print("\nCreating narrower ranges for accurate portions:")

# ============================================================================
# RANGE 1: 1200-1500 cal (Very Light Users - dinju 20kg)
# ============================================================================

# 1200-1500 VEGAN
DietPlanTemplate.objects.create(
    name="Weight Gain - Vegan Light (1200-1500)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day vegan weight gain for very light users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Sweet potato", "quantity": "80g"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "15g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Mango", "quantity": "80g"}, {"food": "Almonds", "quantity": "15g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}],
            "lunch": [{"food": "Quinoa", "quantity": "95g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "15g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Sweet potato", "quantity": "80g"}, {"food": "Almonds", "quantity": "15g"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Mango", "quantity": "80g"}, {"food": "Walnuts", "quantity": "15g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "15g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "90g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}]
        }
    }
)
print("✓ Created: Weight Gain - Vegan Light (1200-1500)")

# 1200-1500 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Weight Gain - Vegetarian Light (1200-1500)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day vegetarian weight gain for very light users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "60g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Spinach", "quantity": "70g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "70g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "1 piece"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Paneer", "quantity": "50g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "85g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Spinach", "quantity": "70g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Cashews", "quantity": "12g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "70g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Broccoli", "quantity": "70g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Walnuts", "quantity": "12g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "1 piece"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Gain - Vegetarian Light (1200-1500)")

# 1200-1500 NON-VEG
DietPlanTemplate.objects.create(
    name="Weight Gain - Non-Veg Light (1200-1500)",
    goal_type="weight_gain",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day non-veg weight gain for very light users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Chicken breast", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "60g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Chicken thigh", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "70g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Cashews", "quantity": "12g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "70g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Quinoa", "quantity": "85g"}, {"food": "Chicken breast", "quantity": "90g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Spinach", "quantity": "70g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Chicken thigh", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "12g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Mutton", "quantity": "70g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Walnuts", "quantity": "12g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chicken breast", "quantity": "90g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        }
    }
)
print("✓ Created: Weight Gain - Non-Veg Light (1200-1500)")

# ============================================================================
# RANGE 2: 1500-1800 cal (Medium Users - Sherin, Aiswarya, Priya)
# ============================================================================

# 1500-1800 VEGAN
DietPlanTemplate.objects.create(
    name="Weight Gain - Vegan Medium (1500-1800)",
    goal_type="weight_gain",
    calorie_min=1500,
    calorie_max=1800,
    description="7-day vegan weight gain for medium users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "16g"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Mango", "quantity": "100g"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "16g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}],
            "lunch": [{"food": "Quinoa", "quantity": "115g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "90g"}, {"food": "Tomato", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "18g"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Gain - Vegan Medium (1500-1800)")

# 1500-1800 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Weight Gain - Vegetarian Medium (1500-1800)",
    goal_type="weight_gain",
    calorie_min=1500,
    calorie_max=1800,
    description="7-day vegetarian weight gain for medium users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "105g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Paneer", "quantity": "85g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Mango", "quantity": "70g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "14g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "14g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "65g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Tomato", "quantity": "70g"}, {"food": "Broccoli", "quantity": "60g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Quinoa", "quantity": "105g"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "85g"}, {"food": "Spinach", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "16g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Spinach", "quantity": "60g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "16g"}]
        }
    }
)
print("✓ Created: Weight Gain - Vegetarian Medium (1500-1800)")

# 1500-1800 NON-VEG
DietPlanTemplate.objects.create(
    name="Weight Gain - Non-Veg Medium (1500-1800)",
    goal_type="weight_gain",
    calorie_min=1500,
    calorie_max=1800,
    description="7-day non-veg weight gain for medium users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "110g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Chicken thigh", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Mango", "quantity": "70g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "90g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "60g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken breast", "quantity": "110g"}, {"food": "Broccoli", "quantity": "80g"}, {"food": "Tomato", "quantity": "60g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Chicken thigh", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Paneer", "quantity": "75g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "60g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Mutton", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Walnuts", "quantity": "16g"}, {"food": "Mango", "quantity": "70g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Almonds", "quantity": "14g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chicken breast", "quantity": "110g"}, {"food": "Carrot", "quantity": "100g"}, {"food": "Spinach", "quantity": "60g"}],
            "dinner": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}, {"food": "Orange", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Gain - Non-Veg Medium (1500-1800)")

print("\n" + "=" * 80)
print("FINAL WEIGHT GAIN TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='weight_gain').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")

print("\n" + "=" * 80)
print("USER MATCHING:")
print("=" * 80)
print("  dinju (1200 cal, non_veg)     → Weight Gain - Non-Veg Light (1200-1500)")
print("  Sherin (1508 cal, vegan)      → Weight Gain - Vegan Medium (1500-1800)")
print("  Aiswarya (1700 cal, vegan)    → Weight Gain - Vegan Medium (1500-1800)")
print("  Priya (1724 cal, vegan)       → Weight Gain - Vegan Medium (1500-1800)")
print("\nTotal weight_gain templates: " + str(templates.count()))
