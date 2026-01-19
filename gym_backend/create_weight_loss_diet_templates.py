import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate
import json

print("Creating Diet-Specific Weight Loss Templates")
print("=" * 80)

# Delete old generic weight_loss templates
deleted = DietPlanTemplate.objects.filter(goal_type='weight_loss').delete()
print(f"✓ Deleted {deleted[0]} old generic weight_loss templates")

print("\nCreating diet-specific weight_loss templates:")

# ============================================================================
# RANGE 1: 1500-2000 cal (Most weight loss users)
# ============================================================================

# 1500-2000 VEGAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegan (1500-2000)",
    goal_type="weight_loss",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day vegan weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "12g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "110g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Carrot", "quantity": "80g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Sweet potato", "quantity": "80g"}, {"food": "Walnuts", "quantity": "10g"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "12g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Mango", "quantity": "80g"}, {"food": "Cashews", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Tomato", "quantity": "80g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "12g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "12g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "12g"}],
            "lunch": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Carrot", "quantity": "80g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Sweet potato", "quantity": "80g"}, {"food": "Cashews", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Mango", "quantity": "80g"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "10g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "100g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegan (1500-2000)")

# 1500-2000 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegetarian (1500-2000)",
    goal_type="weight_loss",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day vegetarian weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "90g"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "10g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Tofu", "quantity": "90g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "1 piece"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Walnuts", "quantity": "10g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "90g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Cashews", "quantity": "10g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Tofu", "quantity": "90g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "1 piece"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegetarian (1500-2000)")

# 1500-2000 NON-VEG
DietPlanTemplate.objects.create(
    name="Weight Loss - Non-Veg (1500-2000)",
    goal_type="weight_loss",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day non-veg weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "100g"}, {"food": "Chicken breast", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Carrot", "quantity": "80g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Chicken thigh", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "10g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "80g"}, {"food": "Potato", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "10g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Chicken breast", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "10g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Quinoa", "quantity": "90g"}, {"food": "Chicken thigh", "quantity": "90g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "90g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "80g"}, {"food": "Potato", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "12g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "90g"}, {"food": "Chicken breast", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Loss - Non-Veg (1500-2000)")

# ============================================================================
# RANGE 2: 2000-2500 cal (Heavier weight loss users)
# ============================================================================

# 2000-2500 VEGAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegan High (2000-2500)",
    goal_type="weight_loss",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day vegan weight loss for heavier users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "16g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "95g"}, {"food": "Mango", "quantity": "100g"}, {"food": "Cashews", "quantity": "18g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "16g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "16g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "18g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "95g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegan High (2000-2500)")

# 2000-2500 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegetarian High (2000-2500)",
    goal_type="weight_loss",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day vegetarian weight loss for heavier users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "16g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegetarian High (2000-2500)")

# 2000-2500 NON-VEG
DietPlanTemplate.objects.create(
    name="Weight Loss - Non-Veg High (2000-2500)",
    goal_type="weight_loss",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day non-veg weight loss for heavier users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken thigh", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Black beans", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken thigh", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "80g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "100g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Walnuts", "quantity": "16g"}, {"food": "Mango", "quantity": "80g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Almonds", "quantity": "14g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "18g"}]
        }
    }
)
print("✓ Created: Weight Loss - Non-Veg High (2000-2500)")

print("\n" + "=" * 80)
print("FINAL WEIGHT LOSS TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='weight_loss').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")
print(f"\nTotal weight_loss templates: {templates.count()}")
