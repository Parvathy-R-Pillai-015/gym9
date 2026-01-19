import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import FoodItem

# Update diet types for all food items
# Logic: 
# - Vegan: No animal products (vegetables, fruits, grains, legumes, nuts - except if mixed with dairy)
# - Vegetarian: No meat/seafood, but dairy/eggs OK  
# - Non-veg: Meat and seafood

diet_type_mapping = {
    # Non-veg foods
    'Chicken breast': 'non_veg',
    'Chicken thigh': 'non_veg',
    'Mutton': 'non_veg',
    'Fish (salmon)': 'non_veg',
    'Fish (tuna)': 'non_veg',
    'Prawns': 'non_veg',
    
    # Vegetarian (has dairy/eggs)
    'Milk (whole)': 'vegetarian',
    'Greek yogurt': 'vegetarian',
    'Paneer': 'vegetarian',
    'Eggs (boiled)': 'vegetarian',
    'Eggs (scrambled)': 'vegetarian',
    'Cheese (cheddar)': 'vegetarian',
    'Butter': 'vegetarian',
    'Ghee': 'vegetarian',
    
    # Vegan foods (all others - grains, vegetables, fruits, legumes, nuts without animal products)
    'Oats': 'vegan',
    'Rice (white, cooked)': 'vegan',
    'Rice (brown, cooked)': 'vegan',
    'Roti (wheat)': 'vegan',
    'Bread (whole wheat)': 'vegan',
    'Quinoa': 'vegan',
    'Pasta (cooked)': 'vegan',
    'Sweet potato': 'vegan',
    'Potato': 'vegan',
    'Broccoli': 'vegan',
    'Spinach': 'vegan',
    'Carrot': 'vegan',
    'Tomato': 'vegan',
    'Cucumber': 'vegan',
    'Mixed vegetables': 'vegan',
    'Banana': 'vegan',
    'Apple': 'vegan',
    'Orange': 'vegan',
    'Strawberries': 'vegan',
    'Mango': 'vegan',
    'Tofu': 'vegan',
    'Lentils (cooked)': 'vegan',
    'Chickpeas': 'vegan',
    'Black beans': 'vegan',
    'Kidney beans': 'vegan',
    'Almonds': 'vegan',
    'Walnuts': 'vegan',
    'Peanuts': 'vegan',
    'Cashews': 'vegan',
    'Olive oil': 'vegan',
    'Coconut oil': 'vegan',
    'Honey': 'vegan',  # Some consider it non-vegan, but we'll keep it vegan for now
}

print("Updating food items with diet types...")
print("-" * 70)

updated_count = 0
for food_name, diet_type in diet_type_mapping.items():
    try:
        food = FoodItem.objects.get(name=food_name)
        food.diet_type = diet_type
        food.save()
        print(f"✓ {food_name:30s} → {diet_type}")
        updated_count += 1
    except FoodItem.DoesNotExist:
        print(f"✗ {food_name:30s} → NOT FOUND")

print("-" * 70)
print(f"Updated {updated_count} food items")

# Show summary by diet type
print("\n" + "=" * 70)
print("SUMMARY BY DIET TYPE:")
print("=" * 70)
vegan = FoodItem.objects.filter(diet_type='vegan').count()
vegetarian = FoodItem.objects.filter(diet_type='vegetarian').count()
non_veg = FoodItem.objects.filter(diet_type='non_veg').count()

print(f"Vegan foods:       {vegan:3d}")
print(f"Vegetarian foods:  {vegetarian:3d}")
print(f"Non-veg foods:     {non_veg:3d}")
print(f"Total:             {vegan + vegetarian + non_veg:3d}")
