import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate, UserProfile

print("=" * 80)
print("CHECKING MUSCLE GOAL TYPE IN DATABASE")
print("=" * 80)

# Check what goal values are actually used
goals = UserProfile.objects.values_list('goal', flat=True).distinct()
print(f"\nGoals in database: {list(goals)}")

# Check existing templates
print("\n" + "=" * 80)
print("EXISTING TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.all().values_list('goal_type', 'name')
for goal, name in templates:
    print(f"  {goal:20s} | {name}")

# Check Vishnu's profile
vishnu = UserProfile.objects.filter(user__name='Vishnu').first()
if vishnu:
    print(f"\n" + "=" * 80)
    print(f"VISHNU'S PROFILE:")
    print("=" * 80)
    print(f"  Goal: {vishnu.goal}")
    print(f"  Weight: {vishnu.current_weight}kg")
    print(f"  Diet: {vishnu.diet_preference}")
    
    # Calculate calories
    target_calories = int(vishnu.current_weight * 30)
    print(f"  Target calories (muscle_building): {target_calories} cal")

print("\n" + "=" * 80)
print("CREATING MUSCLE_BUILDING TEMPLATES (diet-specific)")
print("=" * 80)

# Delete old muscle_building templates
deleted = DietPlanTemplate.objects.filter(goal_type='muscle_building').delete()
print(f"✓ Deleted {deleted[0]} old muscle_building templates")

# Create 1500-2000 cal range (for lighter users)
DietPlanTemplate.objects.create(
    name="Muscle Building - Vegan (1500-2000)",
    goal_type="muscle_building",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day vegan muscle building with high protein",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "20g"}, {"food": "Peanuts", "quantity": "15g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "120g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Black beans", "quantity": "80g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "18g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Mango", "quantity": "100g"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "2 medium"}, {"food": "Cashews", "quantity": "18g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "20g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "18g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "80g"}, {"food": "Banana", "quantity": "2 medium"}, {"food": "Almonds", "quantity": "18g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Tofu", "quantity": "110g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "20g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Sweet potato", "quantity": "100g"}, {"food": "Walnuts", "quantity": "18g"}],
            "lunch": [{"food": "Quinoa", "quantity": "120g"}, {"food": "Black beans", "quantity": "130g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Mango", "quantity": "100g"}, {"food": "Peanuts", "quantity": "22g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "85g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "20g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "120g"}, {"food": "Lentils (cooked)", "quantity": "130g"}, {"food": "Tofu", "quantity": "100g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Black beans", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Muscle Building - Vegan (1500-2000)")

DietPlanTemplate.objects.create(
    name="Muscle Building - Vegetarian (1500-2000)",
    goal_type="muscle_building",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day vegetarian muscle building with high protein",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "15g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Paneer", "quantity": "90g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Almonds", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "15g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "15g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Paneer", "quantity": "70g"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "120g"}, {"food": "Tofu", "quantity": "90g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "70g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Almonds", "quantity": "15g"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Peanuts", "quantity": "18g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "75g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Milk (whole)", "quantity": "200ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Paneer", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "120g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "16g"}]
        }
    }
)
print("✓ Created: Muscle Building - Vegetarian (1500-2000)")

DietPlanTemplate.objects.create(
    name="Muscle Building - Non-Veg (1500-2000)",
    goal_type="muscle_building",
    calorie_min=1500,
    calorie_max=2000,
    description="7-day non-veg muscle building with high protein",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "120g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "15g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken thigh", "quantity": "120g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "110g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Walnuts", "quantity": "12g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Broccoli", "quantity": "90g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "16g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Almonds", "quantity": "16g"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "60g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Quinoa", "quantity": "110g"}, {"food": "Chicken thigh", "quantity": "120g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "110g"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Cashews", "quantity": "16g"}, {"food": "Apple", "quantity": "1 medium"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "3 slices"}, {"food": "Eggs (scrambled)", "quantity": "3 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Mutton", "quantity": "110g"}, {"food": "Potato", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "100g"}, {"food": "Chickpeas (cooked)", "quantity": "110g"}, {"food": "Carrot", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "200ml"}, {"food": "Walnuts", "quantity": "16g"}, {"food": "Banana", "quantity": "1 medium"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "65g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "3 pieces"}, {"food": "Almonds", "quantity": "14g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "110g"}, {"food": "Chicken breast", "quantity": "130g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "3 pieces"}, {"food": "Lentils (cooked)", "quantity": "110g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Eggs (boiled)", "quantity": "2 pieces"}, {"food": "Peanuts", "quantity": "18g"}, {"food": "Apple", "quantity": "1 medium"}]
        }
    }
)
print("✓ Created: Muscle Building - Non-Veg (1500-2000)")

print("\n" + "=" * 80)
print("FINAL MUSCLE_BUILDING TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='muscle_building').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")
print(f"\nTotal muscle_building templates: {templates.count()}")
