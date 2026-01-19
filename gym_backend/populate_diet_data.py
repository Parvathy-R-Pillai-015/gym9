"""
Script to populate food items and diet plan templates
Run: python populate_diet_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import FoodItem, DietPlanTemplate

def populate_food_items():
    """Add common food items with nutritional data"""
    foods = [
        # Dairy
        {'name': 'Milk (whole)', 'category': 'dairy', 'calories': 61, 'protein': 3.2, 'carbs': 4.8, 'fats': 3.3},
        {'name': 'Yogurt (plain)', 'category': 'dairy', 'calories': 59, 'protein': 3.5, 'carbs': 4.7, 'fats': 3.3},
        {'name': 'Paneer', 'category': 'dairy', 'calories': 265, 'protein': 18, 'carbs': 1.2, 'fats': 20.8},
        {'name': 'Cheese (cheddar)', 'category': 'dairy', 'calories': 402, 'protein': 25, 'carbs': 1.3, 'fats': 33},
        
        # Eggs
        {'name': 'Egg (whole)', 'category': 'eggs', 'calories': 155, 'protein': 13, 'carbs': 1.1, 'fats': 11},
        {'name': 'Egg white', 'category': 'eggs', 'calories': 52, 'protein': 11, 'carbs': 0.7, 'fats': 0.2},
        
        # Meat
        {'name': 'Chicken breast', 'category': 'meat', 'calories': 165, 'protein': 31, 'carbs': 0, 'fats': 3.6},
        {'name': 'Chicken thigh', 'category': 'meat', 'calories': 209, 'protein': 26, 'carbs': 0, 'fats': 11},
        {'name': 'Mutton', 'category': 'meat', 'calories': 294, 'protein': 25, 'carbs': 0, 'fats': 21},
        
        # Seafood
        {'name': 'Fish (salmon)', 'category': 'seafood', 'calories': 208, 'protein': 20, 'carbs': 0, 'fats': 13},
        {'name': 'Fish (tuna)', 'category': 'seafood', 'calories': 132, 'protein': 28, 'carbs': 0, 'fats': 1.3},
        {'name': 'Prawns', 'category': 'seafood', 'calories': 99, 'protein': 24, 'carbs': 0.2, 'fats': 0.3},
        
        # Grains
        {'name': 'Rice (white, cooked)', 'category': 'grains', 'calories': 130, 'protein': 2.7, 'carbs': 28, 'fats': 0.3},
        {'name': 'Rice (brown, cooked)', 'category': 'grains', 'calories': 111, 'protein': 2.6, 'carbs': 23, 'fats': 0.9},
        {'name': 'Roti (wheat)', 'category': 'grains', 'calories': 71, 'protein': 3, 'carbs': 15, 'fats': 0.4},
        {'name': 'Oats', 'category': 'grains', 'calories': 389, 'protein': 17, 'carbs': 66, 'fats': 7},
        {'name': 'Bread (whole wheat)', 'category': 'grains', 'calories': 247, 'protein': 13, 'carbs': 41, 'fats': 3.4},
        {'name': 'Quinoa', 'category': 'grains', 'calories': 120, 'protein': 4.4, 'carbs': 21, 'fats': 1.9},
        
        # Vegetables
        {'name': 'Broccoli', 'category': 'vegetables', 'calories': 34, 'protein': 2.8, 'carbs': 7, 'fats': 0.4},
        {'name': 'Spinach', 'category': 'vegetables', 'calories': 23, 'protein': 2.9, 'carbs': 3.6, 'fats': 0.4},
        {'name': 'Carrot', 'category': 'vegetables', 'calories': 41, 'protein': 0.9, 'carbs': 10, 'fats': 0.2},
        {'name': 'Tomato', 'category': 'vegetables', 'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'fats': 0.2},
        {'name': 'Potato', 'category': 'vegetables', 'calories': 77, 'protein': 2, 'carbs': 17, 'fats': 0.1},
        {'name': 'Sweet potato', 'category': 'vegetables', 'calories': 86, 'protein': 1.6, 'carbs': 20, 'fats': 0.1},
        
        # Fruits
        {'name': 'Banana', 'category': 'fruits', 'calories': 89, 'protein': 1.1, 'carbs': 23, 'fats': 0.3},
        {'name': 'Apple', 'category': 'fruits', 'calories': 52, 'protein': 0.3, 'carbs': 14, 'fats': 0.2},
        {'name': 'Orange', 'category': 'fruits', 'calories': 47, 'protein': 0.9, 'carbs': 12, 'fats': 0.1},
        {'name': 'Mango', 'category': 'fruits', 'calories': 60, 'protein': 0.8, 'carbs': 15, 'fats': 0.4},
        {'name': 'Papaya', 'category': 'fruits', 'calories': 43, 'protein': 0.5, 'carbs': 11, 'fats': 0.3},
        
        # Legumes
        {'name': 'Lentils (cooked)', 'category': 'legumes', 'calories': 116, 'protein': 9, 'carbs': 20, 'fats': 0.4},
        {'name': 'Chickpeas (cooked)', 'category': 'legumes', 'calories': 164, 'protein': 8.9, 'carbs': 27, 'fats': 2.6},
        {'name': 'Black beans', 'category': 'legumes', 'calories': 132, 'protein': 8.9, 'carbs': 24, 'fats': 0.5},
        {'name': 'Tofu', 'category': 'legumes', 'calories': 76, 'protein': 8, 'carbs': 1.9, 'fats': 4.8},
        
        # Nuts
        {'name': 'Almonds', 'category': 'nuts', 'calories': 579, 'protein': 21, 'carbs': 22, 'fats': 50},
        {'name': 'Walnuts', 'category': 'nuts', 'calories': 654, 'protein': 15, 'carbs': 14, 'fats': 65},
        {'name': 'Peanuts', 'category': 'nuts', 'calories': 567, 'protein': 26, 'carbs': 16, 'fats': 49},
        {'name': 'Cashews', 'category': 'nuts', 'calories': 553, 'protein': 18, 'carbs': 30, 'fats': 44},
    ]
    
    created_count = 0
    for food in foods:
        obj, created = FoodItem.objects.get_or_create(
            name=food['name'],
            defaults={
                'food_category': food['category'],
                'calories': food['calories'],
                'protein': food['protein'],
                'carbs': food['carbs'],
                'fats': food['fats']
            }
        )
        if created:
            created_count += 1
    
    print(f"✅ Created {created_count} food items (Total: {FoodItem.objects.count()})")


def populate_diet_templates():
    """Create diet plan templates for different goals"""
    
    templates = [
        # WEIGHT LOSS PLANS
        {
            'name': 'Weight Loss - Low Calorie (1200-1500)',
            'goal_type': 'weight_loss',
            'calorie_min': 1200,
            'calorie_max': 1500,
            'description': 'Low calorie plan for rapid weight loss',
            'meals_data': {
                'breakfast': [
                    {'food': 'Oats', 'quantity': '50g', 'calories': 195},
                    {'food': 'Banana', 'quantity': '1 medium', 'calories': 105},
                    {'food': 'Almonds', 'quantity': '10g', 'calories': 58}
                ],
                'lunch': [
                    {'food': 'Chicken breast', 'quantity': '100g', 'calories': 165},
                    {'food': 'Rice (brown, cooked)', 'quantity': '100g', 'calories': 111},
                    {'food': 'Broccoli', 'quantity': '100g', 'calories': 34}
                ],
                'dinner': [
                    {'food': 'Fish (tuna)', 'quantity': '100g', 'calories': 132},
                    {'food': 'Spinach', 'quantity': '100g', 'calories': 23},
                    {'food': 'Roti (wheat)', 'quantity': '2 pieces', 'calories': 142}
                ],
                'snacks': [
                    {'food': 'Apple', 'quantity': '1 medium', 'calories': 95},
                    {'food': 'Yogurt (plain)', 'quantity': '100g', 'calories': 59}
                ]
            }
        },
        {
            'name': 'Weight Loss - Moderate (1500-1800)',
            'goal_type': 'weight_loss',
            'calorie_min': 1500,
            'calorie_max': 1800,
            'description': 'Balanced plan for steady weight loss',
            'meals_data': {
                'breakfast': [
                    {'food': 'Egg (whole)', 'quantity': '2 pieces', 'calories': 310},
                    {'food': 'Bread (whole wheat)', 'quantity': '2 slices', 'calories': 160},
                    {'food': 'Orange', 'quantity': '1 medium', 'calories': 62}
                ],
                'lunch': [
                    {'food': 'Chicken thigh', 'quantity': '150g', 'calories': 314},
                    {'food': 'Rice (white, cooked)', 'quantity': '150g', 'calories': 195},
                    {'food': 'Mixed vegetables', 'quantity': '100g', 'calories': 50}
                ],
                'dinner': [
                    {'food': 'Lentils (cooked)', 'quantity': '200g', 'calories': 232},
                    {'food': 'Roti (wheat)', 'quantity': '2 pieces', 'calories': 142},
                    {'food': 'Yogurt (plain)', 'quantity': '100g', 'calories': 59}
                ],
                'snacks': [
                    {'food': 'Almonds', 'quantity': '15g', 'calories': 87},
                    {'food': 'Papaya', 'quantity': '100g', 'calories': 43}
                ]
            }
        },
        
        # WEIGHT GAIN PLANS
        {
            'name': 'Weight Gain - Moderate (2000-2500)',
            'goal_type': 'weight_gain',
            'calorie_min': 2000,
            'calorie_max': 2500,
            'description': 'Balanced plan for healthy weight gain',
            'meals_data': {
                'breakfast': [
                    {'food': 'Oats', 'quantity': '80g', 'calories': 311},
                    {'food': 'Banana', 'quantity': '2 pieces', 'calories': 210},
                    {'food': 'Peanuts', 'quantity': '20g', 'calories': 113},
                    {'food': 'Milk (whole)', 'quantity': '250ml', 'calories': 153}
                ],
                'lunch': [
                    {'food': 'Chicken breast', 'quantity': '200g', 'calories': 330},
                    {'food': 'Rice (white, cooked)', 'quantity': '250g', 'calories': 325},
                    {'food': 'Chickpeas (cooked)', 'quantity': '100g', 'calories': 164},
                    {'food': 'Paneer', 'quantity': '50g', 'calories': 133}
                ],
                'dinner': [
                    {'food': 'Mutton', 'quantity': '150g', 'calories': 441},
                    {'food': 'Roti (wheat)', 'quantity': '4 pieces', 'calories': 284},
                    {'food': 'Potato', 'quantity': '100g', 'calories': 77}
                ],
                'snacks': [
                    {'food': 'Mango', 'quantity': '200g', 'calories': 120},
                    {'food': 'Cashews', 'quantity': '20g', 'calories': 111}
                ]
            }
        },
        {
            'name': 'Weight Gain - High Calorie (2500-3000)',
            'goal_type': 'weight_gain',
            'calorie_min': 2500,
            'calorie_max': 3000,
            'description': 'High calorie plan for rapid weight gain',
            'meals_data': {
                'breakfast': [
                    {'food': 'Egg (whole)', 'quantity': '4 pieces', 'calories': 620},
                    {'food': 'Bread (whole wheat)', 'quantity': '4 slices', 'calories': 320},
                    {'food': 'Cheese (cheddar)', 'quantity': '30g', 'calories': 121},
                    {'food': 'Milk (whole)', 'quantity': '300ml', 'calories': 183}
                ],
                'lunch': [
                    {'food': 'Chicken thigh', 'quantity': '250g', 'calories': 523},
                    {'food': 'Rice (white, cooked)', 'quantity': '300g', 'calories': 390},
                    {'food': 'Paneer', 'quantity': '100g', 'calories': 265}
                ],
                'dinner': [
                    {'food': 'Fish (salmon)', 'quantity': '200g', 'calories': 416},
                    {'food': 'Sweet potato', 'quantity': '200g', 'calories': 172},
                    {'food': 'Roti (wheat)', 'quantity': '3 pieces', 'calories': 213}
                ],
                'snacks': [
                    {'food': 'Banana', 'quantity': '2 pieces', 'calories': 210},
                    {'food': 'Almonds', 'quantity': '30g', 'calories': 174},
                    {'food': 'Yogurt (plain)', 'quantity': '200g', 'calories': 118}
                ]
            }
        },
        
        # MUSCLE BUILDING PLANS
        {
            'name': 'Muscle Building - Moderate (2200-2700)',
            'goal_type': 'muscle_building',
            'calorie_min': 2200,
            'calorie_max': 2700,
            'description': 'High protein plan for muscle gain',
            'meals_data': {
                'breakfast': [
                    {'food': 'Egg (whole)', 'quantity': '4 pieces', 'calories': 620},
                    {'food': 'Oats', 'quantity': '60g', 'calories': 233},
                    {'food': 'Banana', 'quantity': '1 piece', 'calories': 105}
                ],
                'lunch': [
                    {'food': 'Chicken breast', 'quantity': '250g', 'calories': 413},
                    {'food': 'Quinoa', 'quantity': '150g', 'calories': 180},
                    {'food': 'Broccoli', 'quantity': '150g', 'calories': 51},
                    {'food': 'Sweet potato', 'quantity': '150g', 'calories': 129}
                ],
                'dinner': [
                    {'food': 'Fish (tuna)', 'quantity': '200g', 'calories': 264},
                    {'food': 'Rice (brown, cooked)', 'quantity': '200g', 'calories': 222},
                    {'food': 'Paneer', 'quantity': '100g', 'calories': 265}
                ],
                'snacks': [
                    {'food': 'Egg white', 'quantity': '4 pieces', 'calories': 208},
                    {'food': 'Almonds', 'quantity': '25g', 'calories': 145},
                    {'food': 'Apple', 'quantity': '1 piece', 'calories': 95}
                ]
            }
        },
        {
            'name': 'Muscle Building - High Protein (2700-3200)',
            'goal_type': 'muscle_building',
            'calorie_min': 2700,
            'calorie_max': 3200,
            'description': 'Very high protein for serious muscle building',
            'meals_data': {
                'breakfast': [
                    {'food': 'Egg (whole)', 'quantity': '5 pieces', 'calories': 775},
                    {'food': 'Oats', 'quantity': '80g', 'calories': 311},
                    {'food': 'Walnuts', 'quantity': '20g', 'calories': 131}
                ],
                'lunch': [
                    {'food': 'Chicken breast', 'quantity': '300g', 'calories': 495},
                    {'food': 'Rice (white, cooked)', 'quantity': '300g', 'calories': 390},
                    {'food': 'Chickpeas (cooked)', 'quantity': '150g', 'calories': 246},
                    {'food': 'Spinach', 'quantity': '100g', 'calories': 23}
                ],
                'dinner': [
                    {'food': 'Fish (salmon)', 'quantity': '250g', 'calories': 520},
                    {'food': 'Quinoa', 'quantity': '200g', 'calories': 240},
                    {'food': 'Paneer', 'quantity': '100g', 'calories': 265}
                ],
                'snacks': [
                    {'food': 'Egg white', 'quantity': '6 pieces', 'calories': 312},
                    {'food': 'Banana', 'quantity': '2 pieces', 'calories': 210},
                    {'food': 'Peanuts', 'quantity': '30g', 'calories': 170}
                ]
            }
        }
    ]
    
    created_count = 0
    for template in templates:
        obj, created = DietPlanTemplate.objects.get_or_create(
            name=template['name'],
            defaults={
                'goal_type': template['goal_type'],
                'calorie_min': template['calorie_min'],
                'calorie_max': template['calorie_max'],
                'description': template['description'],
                'meals_data': template['meals_data']
            }
        )
        if created:
            created_count += 1
    
    print(f"✅ Created {created_count} diet plan templates (Total: {DietPlanTemplate.objects.count()})")


if __name__ == '__main__':
    print("\n🍽️  Populating Food Database...\n")
    populate_food_items()
    print("\n📋 Creating Diet Plan Templates...\n")
    populate_diet_templates()
    print("\n✅ Diet data population complete!\n")
