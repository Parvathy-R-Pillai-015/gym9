import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserLogin, UserProfile, FoodItem

print("=" * 80)
print("TESTING DIET PREFERENCE FILTERING")
print("=" * 80)

# Test users with different diet preferences
test_users = [
    ('Sherin', 'vegan'),
    ('KRISHNA', 'vegetarian'),
    ('dinju', 'non_veg'),
]

for user_name, expected_pref in test_users:
    user = UserLogin.objects.filter(name=user_name).first()
    if not user:
        continue
        
    profile = UserProfile.objects.get(user=user)
    
    print(f"\n{user_name.upper()} - {profile.diet_preference.upper()}")
    print(f"Allergies: {profile.food_allergies or 'None'}")
    print("-" * 80)
    
    # Simulate API filtering logic
    foods = FoodItem.objects.all()
    
    # Filter by diet preference
    if profile.diet_preference == 'vegan':
        foods = foods.filter(diet_type='vegan')
    elif profile.diet_preference == 'vegetarian':
        foods = foods.filter(diet_type__in=['vegan', 'vegetarian'])
    # non_veg gets all foods
    
    # Filter allergies
    if profile.food_allergies:
        allergies = [a.strip().lower() for a in profile.food_allergies.split(',')]
        allergy_category_map = {
            'milk': 'dairy',
            'dairy': 'dairy',
            'seafood': 'seafood',
            'fish': 'seafood',
            'nuts': 'nuts',
            'eggs': 'eggs',
            'egg': 'eggs'
        }
        
        excluded_categories = []
        for allergy in allergies:
            if allergy in allergy_category_map:
                excluded_categories.append(allergy_category_map[allergy])
        
        if excluded_categories:
            foods = foods.exclude(food_category__in=excluded_categories)
    
    print(f"Available foods: {foods.count()}")
    
    # Show sample foods by category
    categories = ['grains', 'vegetables', 'fruits', 'meat', 'seafood', 'dairy', 'legumes']
    for cat in categories:
        cat_foods = foods.filter(food_category=cat)
        if cat_foods.exists():
            food_names = ', '.join([f.name for f in cat_foods[:3]])
            if cat_foods.count() > 3:
                food_names += f'... (+{cat_foods.count()-3} more)'
            print(f"  {cat.capitalize():12s}: {food_names}")

print("\n" + "=" * 80)
