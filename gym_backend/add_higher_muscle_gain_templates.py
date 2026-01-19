import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate

print("=" * 80)
print("CREATING HIGHER CALORIE MUSCLE GAIN TEMPLATES")
print("=" * 80)

# Muscle gain formula: weight * 30
# 50-66kg = 1500-2000 cal (already created)
# 67-83kg = 2000-2500 cal (need to create)
# 84-100kg = 2500-3000 cal (need to create)

# 2000-2500 VEGAN
DietPlanTemplate.objects.create(
    name="Muscle Gain - Vegan High (2000-2500)",
    goal_type="muscle_gain",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day vegan muscle gain for heavier users with high protein",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "100g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "25g"}, {"food": "Peanuts", "quantity": "20g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "160g"}, {"food": "Tofu", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "25g"}, {"food": "Black beans", "quantity": "100g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Sweet potato", "quantity": "120g"}, {"food": "Walnuts", "quantity": "22g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "28g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "105g"}, {"food": "Mango", "quantity": "120g"}, {"food": "Almonds", "quantity": "25g"}],
            "lunch": [{"food": "Quinoa", "quantity": "140g"}, {"food": "Black beans", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Potato", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Peanuts", "quantity": "25g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "150g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Broccoli", "quantity": "90g"}],
            "dinner": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Black beans", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Walnuts", "quantity": "22g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "100g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "22g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "25g"}, {"food": "Banana", "quantity": "2 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Sweet potato", "quantity": "120g"}, {"food": "Walnuts", "quantity": "22g"}],
            "lunch": [{"food": "Quinoa", "quantity": "140g"}, {"food": "Black beans", "quantity": "150g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "120g"}, {"food": "Peanuts", "quantity": "28g"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "105g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "25g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "150g"}, {"food": "Lentils (cooked)", "quantity": "150g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Black beans", "quantity": "140g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Muscle Gain - Vegan High (2000-2500)")

# 2000-2500 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Muscle Gain - Vegetarian High (2000-2500)",
    goal_type="muscle_gain",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day vegetarian muscle gain for heavier users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "250ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Paneer", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Paneer", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Almonds", "quantity": "22g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "95g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "250ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Paneer", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "140g"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Carrot", "quantity": "90g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Banana", "quantity": "2 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "90g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Paneer", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "200ml"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Mango", "quantity": "100g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Paneer", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Banana", "quantity": "2 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "95g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Milk (whole)", "quantity": "250ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Paneer", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "140g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Muscle Gain - Vegetarian High (2000-2500)")

# 2000-2500 NON-VEG
DietPlanTemplate.objects.create(
    name="Muscle Gain - Non-Veg High (2000-2500)",
    goal_type="muscle_gain",
    calorie_min=2000,
    calorie_max=2500,
    description="7-day non-veg muscle gain for heavier users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Eggs (boiled)", "quantity": "4 pieces"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "150g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "4 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Chicken thigh", "quantity": "140g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Chickpeas (cooked)", "quantity": "130g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Mango", "quantity": "80g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "4 pieces"}, {"food": "Walnuts", "quantity": "15g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Mutton", "quantity": "130g"}, {"food": "Potato", "quantity": "120g"}],
            "dinner": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "4 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "130g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Eggs (boiled)", "quantity": "4 pieces"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "130g"}, {"food": "Chicken thigh", "quantity": "140g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "140g"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "4 slices"}, {"food": "Eggs (scrambled)", "quantity": "4 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Mutton", "quantity": "130g"}, {"food": "Potato", "quantity": "120g"}],
            "dinner": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "130g"}, {"food": "Carrot", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "250ml"}, {"food": "Walnuts", "quantity": "20g"}, {"food": "Banana", "quantity": "2 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "4 pieces"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "140g"}, {"food": "Chicken breast", "quantity": "150g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "4 pieces"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Muscle Gain - Non-Veg High (2000-2500)")

print("\n" + "=" * 80)
print("ALL MUSCLE_GAIN TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='muscle_gain').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")

print(f"\nTotal muscle_gain templates: {templates.count()}")
print("\nCalorie Coverage:")
print("  1500-2000 cal → Users weighing 50-66kg")
print("  2000-2500 cal → Users weighing 67-83kg")
