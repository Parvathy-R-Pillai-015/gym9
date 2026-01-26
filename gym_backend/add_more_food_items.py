"""
Additional script to populate more food items to reach 500+
"""

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import FoodItem

# Additional food items for comprehensive coverage
ADDITIONAL_FOODS = [
    # INDIAN SPECIFIC BREADS & ITEMS
    {"name": "Puris", "category": "grains", "diet_type": "vegetarian", "calories": 280, "protein": 5, "carbs": 35, "fats": 13},
    {"name": "Kulcha", "category": "grains", "diet_type": "vegetarian", "calories": 220, "protein": 6, "carbs": 35, "fats": 5},
    {"name": "Bhatura", "category": "grains", "diet_type": "vegetarian", "calories": 240, "protein": 6, "carbs": 38, "fats": 6},
    {"name": "Dhokla", "category": "grains", "diet_type": "vegetarian", "calories": 120, "protein": 3, "carbs": 24, "fats": 1},
    {"name": "Khichdi", "category": "grains", "diet_type": "vegetarian", "calories": 150, "protein": 4, "carbs": 28, "fats": 2},
    {"name": "Idiyappam", "category": "grains", "diet_type": "vegan", "calories": 80, "protein": 1.5, "carbs": 18, "fats": 0.3},
    {"name": "String Hoppers", "category": "grains", "diet_type": "vegan", "calories": 80, "protein": 1.5, "carbs": 18, "fats": 0.3},
    {"name": "Dahi Bhalle", "category": "other", "diet_type": "vegetarian", "calories": 180, "protein": 4, "carbs": 20, "fats": 8},
    
    # REGIONAL CURRIES & GRAVIES
    {"name": "Chole Bhature Gravy", "category": "legumes", "diet_type": "vegetarian", "calories": 140, "protein": 6, "carbs": 16, "fats": 5},
    {"name": "Paneer Tikka Masala", "category": "dairy", "diet_type": "vegetarian", "calories": 220, "protein": 15, "carbs": 8, "fats": 14},
    {"name": "Butter Chicken", "category": "meat", "diet_type": "non_veg", "calories": 240, "protein": 20, "carbs": 6, "fats": 16},
    {"name": "Tandoori Chicken", "category": "meat", "diet_type": "non_veg", "calories": 180, "protein": 28, "carbs": 2, "fats": 7},
    {"name": "Biryani Gravy", "category": "meat", "diet_type": "non_veg", "calories": 200, "protein": 15, "carbs": 12, "fats": 10},
    {"name": "Crab Masala", "category": "seafood", "diet_type": "non_veg", "calories": 160, "protein": 22, "carbs": 4, "fats": 7},
    {"name": "Shrimp Masala", "category": "seafood", "diet_type": "non_veg", "calories": 140, "protein": 24, "carbs": 3, "fats": 3},
    
    # KERALA SPECIFIC ITEMS (EXTENDED)
    {"name": "Appalam", "category": "grains", "diet_type": "vegetarian", "calories": 350, "protein": 15, "carbs": 50, "fats": 10},
    {"name": "Papad", "category": "grains", "diet_type": "vegetarian", "calories": 340, "protein": 14, "carbs": 48, "fats": 10},
    {"name": "Prawn Fry", "category": "seafood", "diet_type": "non_veg", "calories": 200, "protein": 25, "carbs": 2, "fats": 10},
    {"name": "Fish Fry", "category": "seafood", "diet_type": "non_veg", "calories": 220, "protein": 24, "carbs": 3, "fats": 12},
    {"name": "Mutton Fry", "category": "meat", "diet_type": "non_veg", "calories": 280, "protein": 28, "carbs": 2, "fats": 17},
    {"name": "Chicken Fry", "category": "meat", "diet_type": "non_veg", "calories": 240, "protein": 26, "carbs": 2, "fats": 14},
    
    # VEGETABLE CURRIES & PREPARATIONS
    {"name": "Aloo Gobi", "category": "vegetables", "diet_type": "vegan", "calories": 100, "protein": 2, "carbs": 15, "fats": 3.5},
    {"name": "Chana Masala", "category": "legumes", "diet_type": "vegan", "calories": 180, "protein": 8, "carbs": 20, "fats": 7},
    {"name": "Baingan Bharta", "category": "vegetables", "diet_type": "vegetarian", "calories": 120, "protein": 2, "carbs": 12, "fats": 6},
    {"name": "Sag Paneer", "category": "dairy", "diet_type": "vegetarian", "calories": 180, "protein": 14, "carbs": 6, "fats": 11},
    {"name": "Malai Kofta", "category": "vegetables", "diet_type": "vegetarian", "calories": 200, "protein": 5, "carbs": 15, "fats": 13},
    {"name": "Vegetable Jalfrezi", "category": "vegetables", "diet_type": "vegan", "calories": 110, "protein": 3, "carbs": 16, "fats": 4},
    {"name": "Cauliflower 65", "category": "vegetables", "diet_type": "vegetarian", "calories": 240, "protein": 4, "carbs": 20, "fats": 15},
    {"name": "Paneer 65", "category": "dairy", "diet_type": "vegetarian", "calories": 280, "protein": 16, "carbs": 18, "fats": 17},
    
    # LENTIL DISHES
    {"name": "Dal Tadka", "category": "legumes", "diet_type": "vegan", "calories": 130, "protein": 6, "carbs": 18, "fats": 3},
    {"name": "Dal Makhani", "category": "legumes", "diet_type": "vegetarian", "calories": 200, "protein": 8, "carbs": 16, "fats": 12},
    {"name": "Rajma", "category": "legumes", "diet_type": "vegan", "calories": 140, "protein": 7, "carbs": 20, "fats": 2},
    {"name": "Chole", "category": "legumes", "diet_type": "vegan", "calories": 160, "protein": 8, "carbs": 24, "fats": 2.5},
    
    # RICE PREPARATIONS
    {"name": "Pulao with Vegetables", "category": "grains", "diet_type": "vegetarian", "calories": 180, "protein": 4, "carbs": 32, "fats": 4},
    {"name": "Chicken Pulao", "category": "grains", "diet_type": "non_veg", "calories": 250, "protein": 12, "carbs": 32, "fats": 8},
    {"name": "Mutton Biryani", "category": "grains", "diet_type": "non_veg", "calories": 300, "protein": 14, "carbs": 40, "fats": 10},
    {"name": "Prawn Biryani", "category": "grains", "diet_type": "non_veg", "calories": 280, "protein": 16, "carbs": 38, "fats": 9},
    {"name": "Veg Biryani", "category": "grains", "diet_type": "vegetarian", "calories": 200, "protein": 5, "carbs": 36, "fats": 4},
    
    # SOUPS & BROTHS
    {"name": "Chicken Soup", "category": "meat", "diet_type": "non_veg", "calories": 60, "protein": 8, "carbs": 3, "fats": 2},
    {"name": "Vegetable Soup", "category": "vegetables", "diet_type": "vegan", "calories": 35, "protein": 1.5, "carbs": 6, "fats": 0.5},
    {"name": "Tomato Soup", "category": "vegetables", "diet_type": "vegan", "calories": 45, "protein": 1, "carbs": 8, "fats": 1.5},
    {"name": "Corn Soup", "category": "vegetables", "diet_type": "vegetarian", "calories": 80, "protein": 2, "carbs": 14, "fats": 2},
    {"name": "Mushroom Soup", "category": "vegetables", "diet_type": "vegetarian", "calories": 60, "protein": 2, "carbs": 8, "fats": 2},
    
    # SEAFOOD ITEMS
    {"name": "Cuttlefish", "category": "seafood", "diet_type": "non_veg", "calories": 92, "protein": 15, "carbs": 3, "fats": 1.4},
    {"name": "Clams", "category": "seafood", "diet_type": "non_veg", "calories": 86, "protein": 15, "carbs": 3, "fats": 1.3},
    {"name": "Oysters", "category": "seafood", "diet_type": "non_veg", "calories": 68, "protein": 7, "carbs": 4, "fats": 2},
    {"name": "Mussels", "category": "seafood", "diet_type": "non_veg", "calories": 72, "protein": 12, "carbs": 3, "fats": 2},
    
    # SPROUTS & SEEDS
    {"name": "Moong Sprouts", "category": "legumes", "diet_type": "vegan", "calories": 30, "protein": 3, "carbs": 4, "fats": 0.2},
    {"name": "Alfalfa Sprouts", "category": "vegetables", "diet_type": "vegan", "calories": 23, "protein": 2.7, "carbs": 2, "fats": 0.6},
    {"name": "Mung Bean Sprouts", "category": "legumes", "diet_type": "vegan", "calories": 30, "protein": 3, "carbs": 4, "fats": 0.2},
    
    # GRAINS & CEREALS (ADDITIONAL)
    {"name": "Quinoa", "category": "grains", "diet_type": "vegan", "calories": 120, "protein": 4.4, "carbs": 21.3, "fats": 1.9},
    {"name": "Amaranth", "category": "grains", "diet_type": "vegan", "calories": 102, "protein": 3.7, "carbs": 18.7, "fats": 2.1},
    {"name": "Millet", "category": "grains", "diet_type": "vegan", "calories": 119, "protein": 3.5, "carbs": 23, "fats": 1},
    {"name": "Buckwheat", "category": "grains", "diet_type": "vegan", "calories": 343, "protein": 13.3, "carbs": 71.5, "fats": 3.4},
    
    # DRIED FRUITS
    {"name": "Dried Apricots", "category": "fruits", "diet_type": "vegan", "calories": 268, "protein": 3.4, "carbs": 63, "fats": 0.5},
    {"name": "Dried Figs", "category": "fruits", "diet_type": "vegan", "calories": 249, "protein": 3.3, "carbs": 63.9, "fats": 0.9},
    {"name": "Dried Dates", "category": "fruits", "diet_type": "vegan", "calories": 282, "protein": 2.7, "carbs": 75, "fats": 0.4},
    {"name": "Dried Mango", "category": "fruits", "diet_type": "vegan", "calories": 322, "protein": 1.6, "carbs": 80, "fats": 0.8},
    {"name": "Dried Pineapple", "category": "fruits", "diet_type": "vegan", "calories": 320, "protein": 0.6, "carbs": 84, "fats": 0.3},
    {"name": "Cranberries (dried)", "category": "fruits", "diet_type": "vegan", "calories": 308, "protein": 0.4, "carbs": 82, "fats": 1.5},
    
    # INTERNATIONAL FOODS (COMMON IN INDIA)
    {"name": "Pizza", "category": "grains", "diet_type": "non_veg", "calories": 285, "protein": 12, "carbs": 36, "fats": 10},
    {"name": "Burger", "category": "meat", "diet_type": "non_veg", "calories": 295, "protein": 15, "carbs": 28, "fats": 14},
    {"name": "Hot Dog", "category": "meat", "diet_type": "non_veg", "calories": 290, "protein": 10, "carbs": 26, "fats": 17},
    {"name": "Sandwich (Veg)", "category": "vegetables", "diet_type": "vegan", "calories": 220, "protein": 6, "carbs": 32, "fats": 8},
    {"name": "Salad (Green)", "category": "vegetables", "diet_type": "vegan", "calories": 50, "protein": 2, "carbs": 8, "fats": 1},
    {"name": "Caesar Salad", "category": "vegetables", "diet_type": "non_veg", "calories": 180, "protein": 8, "carbs": 6, "fats": 14},
    
    # SNACK ITEMS (ADDITIONAL)
    {"name": "Corn Puffs", "category": "grains", "diet_type": "vegan", "calories": 580, "protein": 8, "carbs": 52, "fats": 35},
    {"name": "Cheetos", "category": "other", "diet_type": "non_veg", "calories": 590, "protein": 8, "carbs": 54, "fats": 35},
    {"name": "Doritos", "category": "other", "diet_type": "vegan", "calories": 570, "protein": 7, "carbs": 56, "fats": 32},
    {"name": "Lays Chips", "category": "other", "diet_type": "vegan", "calories": 536, "protein": 6, "carbs": 50, "fats": 35},
    {"name": "Kurkure", "category": "other", "diet_type": "vegan", "calories": 530, "protein": 7, "carbs": 54, "fats": 31},
    
    # TRADITIONAL SWEETS
    {"name": "Gulab Jamun", "category": "other", "diet_type": "vegetarian", "calories": 320, "protein": 2, "carbs": 50, "fats": 11},
    {"name": "Ras Malai", "category": "other", "diet_type": "vegetarian", "calories": 260, "protein": 4, "carbs": 40, "fats": 8},
    {"name": "Jalebi", "category": "other", "diet_type": "vegan", "calories": 340, "protein": 1, "carbs": 84, "fats": 1},
    {"name": "Kaju Katli", "category": "other", "diet_type": "vegetarian", "calories": 530, "protein": 14, "carbs": 54, "fats": 28},
    {"name": "Rasgulla", "category": "other", "diet_type": "vegetarian", "calories": 220, "protein": 3, "carbs": 44, "fats": 2},
    
    # PICKLES & CONDIMENTS
    {"name": "Mango Pickle", "category": "fruits", "diet_type": "vegan", "calories": 160, "protein": 1, "carbs": 35, "fats": 1},
    {"name": "Lime Pickle", "category": "fruits", "diet_type": "vegan", "calories": 120, "protein": 0.5, "carbs": 25, "fats": 0.5},
    {"name": "Ginger Pickle", "category": "vegetables", "diet_type": "vegan", "calories": 140, "protein": 1, "carbs": 30, "fats": 1},
    {"name": "Garlic Pickle", "category": "vegetables", "diet_type": "vegan", "calories": 150, "protein": 1.5, "carbs": 32, "fats": 1},
    
    # FORTIFIED FOODS
    {"name": "Fortified Milk", "category": "dairy", "diet_type": "vegetarian", "calories": 70, "protein": 3.5, "carbs": 5, "fats": 3.6},
    {"name": "Fortified Cereal", "category": "grains", "diet_type": "vegetarian", "calories": 360, "protein": 8, "carbs": 82, "fats": 2},
    {"name": "Fortified Bread", "category": "grains", "diet_type": "vegan", "calories": 85, "protein": 2.7, "carbs": 15, "fats": 1.2},
    
    # VEGETABLE JUICE
    {"name": "Beetroot Juice", "category": "vegetables", "diet_type": "vegan", "calories": 40, "protein": 1, "carbs": 9, "fats": 0.1},
    {"name": "Carrot and Orange Juice", "category": "vegetables", "diet_type": "vegan", "calories": 55, "protein": 0.8, "carbs": 13, "fats": 0.2},
    {"name": "Cucumber and Mint Juice", "category": "vegetables", "diet_type": "vegan", "calories": 30, "protein": 0.5, "carbs": 6, "fats": 0.1},
    
    # ADDITIONAL SPICES
    {"name": "Saffron", "category": "vegetables", "diet_type": "vegan", "calories": 310, "protein": 11.4, "carbs": 61.5, "fats": 5.9},
    {"name": "Star Anise", "category": "vegetables", "diet_type": "vegan", "calories": 338, "protein": 17.6, "carbs": 50, "fats": 15.9},
    {"name": "Vanilla Extract", "category": "other", "diet_type": "vegan", "calories": 288, "protein": 0, "carbs": 12.7, "fats": 0},
    
    # PROTEINS (ADDITIONAL)
    {"name": "Cottage Cheese", "category": "dairy", "diet_type": "vegetarian", "calories": 98, "protein": 11, "carbs": 3.4, "fats": 5},
    {"name": "Ricotta", "category": "dairy", "diet_type": "vegetarian", "calories": 174, "protein": 11.3, "carbs": 6.4, "fats": 13},
    {"name": "Tofu", "category": "legumes", "diet_type": "vegan", "calories": 76, "protein": 8.1, "carbs": 1.9, "fats": 4.8},
    {"name": "Tempeh", "category": "legumes", "diet_type": "vegan", "calories": 195, "protein": 19.3, "carbs": 7.6, "fats": 11},
    
    # ADDITIONAL VEGETABLES (TO REACH 500+)
    {"name": "Beet Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 23, "protein": 2.2, "carbs": 4.3, "fats": 0.1},
    {"name": "Pumpkin Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 20, "protein": 1.8, "carbs": 3.2, "fats": 0.2},
    {"name": "Moringa Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 64, "protein": 9.4, "carbs": 8.3, "fats": 1.7},
    {"name": "Dill Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 43, "protein": 3.5, "carbs": 7, "fats": 0.8},
    {"name": "Purslane", "category": "vegetables", "diet_type": "vegan", "calories": 20, "protein": 1.9, "carbs": 3.6, "fats": 0.1},
    {"name": "Chickpea Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 28, "protein": 2.8, "carbs": 4.5, "fats": 0.2},
    {"name": "Spinach Puree", "category": "vegetables", "diet_type": "vegan", "calories": 30, "protein": 3.5, "carbs": 4.5, "fats": 0.5},
    {"name": "Tomato Paste", "category": "vegetables", "diet_type": "vegan", "calories": 82, "protein": 3.9, "carbs": 18.3, "fats": 0.3},
    {"name": "Tomato Sauce", "category": "vegetables", "diet_type": "vegan", "calories": 32, "protein": 1.5, "carbs": 6.5, "fats": 0.3},
]

def populate_additional_foods():
    """Populate additional food items"""
    print(f"Starting to populate {len(ADDITIONAL_FOODS)} additional food items...")
    
    created_count = 0
    skipped_count = 0
    
    for food in ADDITIONAL_FOODS:
        # Check if food already exists
        if FoodItem.objects.filter(name=food['name']).exists():
            skipped_count += 1
            continue
        
        try:
            FoodItem.objects.create(
                name=food['name'],
                food_category=food['category'],
                diet_type=food['diet_type'],
                calories=food['calories'],
                protein=food['protein'],
                carbs=food['carbs'],
                fats=food['fats'],
                serving_size="100g"
            )
            created_count += 1
            if created_count % 50 == 0:
                print(f"Created {created_count} additional foods...")
        except Exception as e:
            print(f"Error creating {food['name']}: {e}")
            skipped_count += 1
    
    print(f"\nPopulation complete!")
    print(f"Created: {created_count} new foods")
    print(f"Skipped: {skipped_count} (already exist)")
    print(f"Total foods in database: {FoodItem.objects.count()}")

if __name__ == '__main__':
    populate_additional_foods()
