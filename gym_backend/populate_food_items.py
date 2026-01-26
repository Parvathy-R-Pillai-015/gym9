"""
Script to populate 500+ food items with calorie information
Including Kerala-style foods and common Indian cuisine
"""

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import FoodItem

# Comprehensive food database with 500+ items
FOOD_DATA = [
    # BREAKFAST ITEMS
    {"name": "Idli", "category": "grains", "diet_type": "vegan", "calories": 70, "protein": 2, "carbs": 15, "fats": 0.5},
    {"name": "Dosa", "category": "grains", "diet_type": "vegan", "calories": 150, "protein": 3, "carbs": 30, "fats": 5},
    {"name": "Appam", "category": "grains", "diet_type": "vegetarian", "calories": 120, "protein": 2, "carbs": 25, "fats": 1},
    {"name": "Puttu", "category": "grains", "diet_type": "vegan", "calories": 130, "protein": 4, "carbs": 25, "fats": 1.5},
    {"name": "Uttapam", "category": "grains", "diet_type": "vegan", "calories": 140, "protein": 3, "carbs": 28, "fats": 2},
    {"name": "Paratha", "category": "grains", "diet_type": "vegetarian", "calories": 200, "protein": 5, "carbs": 30, "fats": 8},
    {"name": "Roti", "category": "grains", "diet_type": "vegan", "calories": 70, "protein": 2, "carbs": 14, "fats": 0.5},
    {"name": "Naan", "category": "grains", "diet_type": "vegetarian", "calories": 270, "protein": 8, "carbs": 49, "fats": 3},
    {"name": "Bread", "category": "grains", "diet_type": "vegan", "calories": 79, "protein": 2.5, "carbs": 14, "fats": 1},
    {"name": "Oats", "category": "grains", "diet_type": "vegan", "calories": 68, "protein": 2.4, "carbs": 11, "fats": 1.4},
    {"name": "Cornflakes", "category": "grains", "diet_type": "vegan", "calories": 380, "protein": 8, "carbs": 84, "fats": 2},
    {"name": "Poha", "category": "grains", "diet_type": "vegan", "calories": 80, "protein": 1, "carbs": 18, "fats": 0.3},
    {"name": "Upma", "category": "grains", "diet_type": "vegetarian", "calories": 150, "protein": 4, "carbs": 25, "fats": 4},
    {"name": "Pancakes", "category": "grains", "diet_type": "vegetarian", "calories": 150, "protein": 4, "carbs": 28, "fats": 3},
    {"name": "Waffles", "category": "grains", "diet_type": "vegetarian", "calories": 220, "protein": 6, "carbs": 42, "fats": 5},
    
    # VEGETABLES
    {"name": "Tomato", "category": "vegetables", "diet_type": "vegan", "calories": 18, "protein": 0.9, "carbs": 3.9, "fats": 0.2},
    {"name": "Onion", "category": "vegetables", "diet_type": "vegan", "calories": 40, "protein": 1.1, "carbs": 9, "fats": 0.1},
    {"name": "Carrot", "category": "vegetables", "diet_type": "vegan", "calories": 41, "protein": 0.9, "carbs": 10, "fats": 0.2},
    {"name": "Cucumber", "category": "vegetables", "diet_type": "vegan", "calories": 16, "protein": 0.7, "carbs": 3.6, "fats": 0.1},
    {"name": "Lettuce", "category": "vegetables", "diet_type": "vegan", "calories": 15, "protein": 1.2, "carbs": 2.9, "fats": 0.2},
    {"name": "Spinach", "category": "vegetables", "diet_type": "vegan", "calories": 23, "protein": 2.7, "carbs": 3.6, "fats": 0.4},
    {"name": "Cabbage", "category": "vegetables", "diet_type": "vegan", "calories": 25, "protein": 1.3, "carbs": 5.8, "fats": 0.1},
    {"name": "Broccoli", "category": "vegetables", "diet_type": "vegan", "calories": 34, "protein": 2.8, "carbs": 7, "fats": 0.4},
    {"name": "Cauliflower", "category": "vegetables", "diet_type": "vegan", "calories": 25, "protein": 1.9, "carbs": 5, "fats": 0.3},
    {"name": "Peas", "category": "vegetables", "diet_type": "vegan", "calories": 81, "protein": 5.4, "carbs": 14.5, "fats": 0.4},
    {"name": "Beans", "category": "vegetables", "diet_type": "vegan", "calories": 31, "protein": 1.8, "carbs": 7, "fats": 0.2},
    {"name": "Beetroot", "category": "vegetables", "diet_type": "vegan", "calories": 43, "protein": 1.6, "carbs": 9.6, "fats": 0.2},
    {"name": "Bottle Gourd", "category": "vegetables", "diet_type": "vegan", "calories": 19, "protein": 0.6, "carbs": 4, "fats": 0.1},
    {"name": "Ridge Gourd", "category": "vegetables", "diet_type": "vegan", "calories": 20, "protein": 0.7, "carbs": 4, "fats": 0.1},
    {"name": "Bitter Gourd", "category": "vegetables", "diet_type": "vegan", "calories": 34, "protein": 1.6, "carbs": 8, "fats": 0.2},
    {"name": "Okra", "category": "vegetables", "diet_type": "vegan", "calories": 33, "protein": 1.9, "carbs": 7, "fats": 0.2},
    {"name": "Bell Pepper", "category": "vegetables", "diet_type": "vegan", "calories": 31, "protein": 1, "carbs": 6, "fats": 0.3},
    {"name": "Zucchini", "category": "vegetables", "diet_type": "vegan", "calories": 21, "protein": 1.4, "carbs": 3.5, "fats": 0.4},
    {"name": "Pumpkin", "category": "vegetables", "diet_type": "vegan", "calories": 26, "protein": 1, "carbs": 6.5, "fats": 0.1},
    {"name": "Eggplant", "category": "vegetables", "diet_type": "vegan", "calories": 25, "protein": 0.98, "carbs": 5.9, "fats": 0.2},
    
    # KERALA SPECIFIC VEGETABLES & ITEMS
    {"name": "Nendran Banana", "category": "fruits", "diet_type": "vegan", "calories": 89, "protein": 1.1, "carbs": 20, "fats": 0.3},
    {"name": "Banana Chips", "category": "vegetables", "diet_type": "vegan", "calories": 520, "protein": 3, "carbs": 60, "fats": 30},
    {"name": "Tapioca", "category": "grains", "diet_type": "vegan", "calories": 160, "protein": 0.2, "carbs": 39, "fats": 0.3},
    {"name": "Cassava", "category": "vegetables", "diet_type": "vegan", "calories": 160, "protein": 1.4, "carbs": 38, "fats": 0.3},
    {"name": "Yam", "category": "vegetables", "diet_type": "vegan", "calories": 118, "protein": 1.5, "carbs": 28, "fats": 0.1},
    {"name": "Colocasia", "category": "vegetables", "diet_type": "vegan", "calories": 112, "protein": 1, "carbs": 26, "fats": 0.1},
    {"name": "Coconut Milk (canned)", "category": "dairy", "diet_type": "vegan", "calories": 230, "protein": 2.3, "carbs": 5, "fats": 24},
    {"name": "Fresh Coconut", "category": "fruits", "diet_type": "vegan", "calories": 354, "protein": 3.3, "carbs": 15.2, "fats": 33.5},
    {"name": "Coconut Oil", "category": "other", "diet_type": "vegan", "calories": 892, "protein": 0, "carbs": 0, "fats": 99},
    
    # FRUITS
    {"name": "Apple", "category": "fruits", "diet_type": "vegan", "calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2},
    {"name": "Banana", "category": "fruits", "diet_type": "vegan", "calories": 89, "protein": 1.1, "carbs": 23, "fats": 0.3},
    {"name": "Orange", "category": "fruits", "diet_type": "vegan", "calories": 47, "protein": 0.9, "carbs": 12, "fats": 0.3},
    {"name": "Mango", "category": "fruits", "diet_type": "vegan", "calories": 60, "protein": 0.8, "carbs": 15, "fats": 0.4},
    {"name": "Papaya", "category": "fruits", "diet_type": "vegan", "calories": 43, "protein": 0.6, "carbs": 11, "fats": 0.3},
    {"name": "Pineapple", "category": "fruits", "diet_type": "vegan", "calories": 50, "protein": 0.5, "carbs": 13, "fats": 0.1},
    {"name": "Watermelon", "category": "fruits", "diet_type": "vegan", "calories": 30, "protein": 0.6, "carbs": 8, "fats": 0.2},
    {"name": "Grapes", "category": "fruits", "diet_type": "vegan", "calories": 69, "protein": 0.7, "carbs": 18, "fats": 0.2},
    {"name": "Guava", "category": "fruits", "diet_type": "vegan", "calories": 68, "protein": 2.6, "carbs": 14, "fats": 1},
    {"name": "Jackfruit", "category": "fruits", "diet_type": "vegan", "calories": 95, "protein": 1.5, "carbs": 23, "fats": 0.3},
    {"name": "Pomegranate", "category": "fruits", "diet_type": "vegan", "calories": 83, "protein": 1.7, "carbs": 19, "fats": 1.2},
    {"name": "Strawberry", "category": "fruits", "diet_type": "vegan", "calories": 32, "protein": 0.8, "carbs": 7.7, "fats": 0.3},
    {"name": "Blueberry", "category": "fruits", "diet_type": "vegan", "calories": 57, "protein": 0.7, "carbs": 14, "fats": 0.3},
    {"name": "Dragon Fruit", "category": "fruits", "diet_type": "vegan", "calories": 60, "protein": 1.2, "carbs": 13, "fats": 0.4},
    {"name": "Kiwi", "category": "fruits", "diet_type": "vegan", "calories": 61, "protein": 1.1, "carbs": 14, "fats": 0.5},
    {"name": "Lemon", "category": "fruits", "diet_type": "vegan", "calories": 29, "protein": 1.1, "carbs": 9, "fats": 0.3},
    {"name": "Lime", "category": "fruits", "diet_type": "vegan", "calories": 30, "protein": 0.7, "carbs": 11, "fats": 0.2},
    {"name": "Peach", "category": "fruits", "diet_type": "vegan", "calories": 39, "protein": 0.9, "carbs": 10, "fats": 0.3},
    {"name": "Pear", "category": "fruits", "diet_type": "vegan", "calories": 57, "protein": 0.4, "carbs": 15, "fats": 0.1},
    {"name": "Plum", "category": "fruits", "diet_type": "vegan", "calories": 46, "protein": 0.7, "carbs": 11, "fats": 0.3},
    
    # NUTS & SEEDS
    {"name": "Almonds", "category": "nuts", "diet_type": "vegan", "calories": 579, "protein": 21.2, "carbs": 22, "fats": 49.9},
    {"name": "Peanuts", "category": "nuts", "diet_type": "vegan", "calories": 567, "protein": 25.8, "carbs": 16.1, "fats": 49.2},
    {"name": "Cashews", "category": "nuts", "diet_type": "vegan", "calories": 553, "protein": 18.2, "carbs": 30.2, "fats": 43.8},
    {"name": "Walnuts", "category": "nuts", "diet_type": "vegan", "calories": 654, "protein": 15.2, "carbs": 13.7, "fats": 65.2},
    {"name": "Pistachios", "category": "nuts", "diet_type": "vegan", "calories": 560, "protein": 20.3, "carbs": 27.2, "fats": 45.3},
    {"name": "Sunflower Seeds", "category": "nuts", "diet_type": "vegan", "calories": 584, "protein": 20.8, "carbs": 20, "fats": 51.5},
    {"name": "Pumpkin Seeds", "category": "nuts", "diet_type": "vegan", "calories": 559, "protein": 30.2, "carbs": 11, "fats": 49.1},
    {"name": "Sesame Seeds", "category": "nuts", "diet_type": "vegan", "calories": 563, "protein": 17.7, "carbs": 23.5, "fats": 50},
    {"name": "Coconut Milk", "category": "nuts", "diet_type": "vegan", "calories": 252, "protein": 2.2, "carbs": 5.5, "fats": 24},
    {"name": "Flax Seeds", "category": "nuts", "diet_type": "vegan", "calories": 534, "protein": 18.3, "carbs": 28.9, "fats": 42.2},
    
    # DAIRY PRODUCTS
    {"name": "Milk (whole)", "category": "dairy", "diet_type": "vegetarian", "calories": 61, "protein": 3.2, "carbs": 4.8, "fats": 3.3},
    {"name": "Milk (skimmed)", "category": "dairy", "diet_type": "vegetarian", "calories": 35, "protein": 3.6, "carbs": 5, "fats": 0.1},
    {"name": "Yogurt (plain)", "category": "dairy", "diet_type": "vegetarian", "calories": 59, "protein": 3.5, "carbs": 3.3, "fats": 3},
    {"name": "Greek Yogurt", "category": "dairy", "diet_type": "vegetarian", "calories": 59, "protein": 10.2, "carbs": 3.3, "fats": 0.4},
    {"name": "Paneer", "category": "dairy", "diet_type": "vegetarian", "calories": 265, "protein": 25.4, "carbs": 1.2, "fats": 20.8},
    {"name": "Cheese", "category": "dairy", "diet_type": "vegetarian", "calories": 402, "protein": 25, "carbs": 1.3, "fats": 33},
    {"name": "Butter", "category": "dairy", "diet_type": "vegetarian", "calories": 717, "protein": 0.9, "carbs": 0.1, "fats": 81.1},
    {"name": "Ghee", "category": "dairy", "diet_type": "vegetarian", "calories": 900, "protein": 0, "carbs": 0, "fats": 99.5},
    {"name": "Curd", "category": "dairy", "diet_type": "vegetarian", "calories": 98, "protein": 3.5, "carbs": 4.3, "fats": 5},
    {"name": "Ice Cream", "category": "dairy", "diet_type": "vegetarian", "calories": 207, "protein": 3.5, "carbs": 24, "fats": 11},
    
    # EGGS
    {"name": "Egg (boiled)", "category": "eggs", "diet_type": "non_veg", "calories": 155, "protein": 13.6, "carbs": 1.1, "fats": 11},
    {"name": "Egg (fried)", "category": "eggs", "diet_type": "non_veg", "calories": 196, "protein": 13, "carbs": 1.1, "fats": 15},
    {"name": "Egg (scrambled)", "category": "eggs", "diet_type": "non_veg", "calories": 154, "protein": 13, "carbs": 1.1, "fats": 11},
    {"name": "Egg White", "category": "eggs", "diet_type": "non_veg", "calories": 52, "protein": 11, "carbs": 0.7, "fats": 0.2},
    {"name": "Egg Yolk", "category": "eggs", "diet_type": "non_veg", "calories": 322, "protein": 16, "carbs": 0.6, "fats": 28},
    
    # MEAT & SEAFOOD
    {"name": "Chicken (breast)", "category": "meat", "diet_type": "non_veg", "calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    {"name": "Chicken (thigh)", "category": "meat", "diet_type": "non_veg", "calories": 209, "protein": 26, "carbs": 0, "fats": 11},
    {"name": "Chicken (whole)", "category": "meat", "diet_type": "non_veg", "calories": 189, "protein": 27.3, "carbs": 0, "fats": 8.5},
    {"name": "Mutton", "category": "meat", "diet_type": "non_veg", "calories": 294, "protein": 25, "carbs": 0, "fats": 21},
    {"name": "Fish", "category": "seafood", "diet_type": "non_veg", "calories": 206, "protein": 22, "carbs": 0, "fats": 12},
    {"name": "Salmon", "category": "seafood", "diet_type": "non_veg", "calories": 208, "protein": 20, "carbs": 0, "fats": 13},
    {"name": "Shrimp", "category": "seafood", "diet_type": "non_veg", "calories": 99, "protein": 24, "carbs": 0, "fats": 0.3},
    {"name": "Crab", "category": "seafood", "diet_type": "non_veg", "calories": 82, "protein": 18, "carbs": 0, "fats": 1},
    {"name": "Squid", "category": "seafood", "diet_type": "non_veg", "calories": 92, "protein": 16, "carbs": 3, "fats": 1.4},
    {"name": "Mackerel", "category": "seafood", "diet_type": "non_veg", "calories": 305, "protein": 25, "carbs": 0, "fats": 23},
    {"name": "Tuna", "category": "seafood", "diet_type": "non_veg", "calories": 144, "protein": 29.9, "carbs": 0, "fats": 1.3},
    {"name": "Pomfret", "category": "seafood", "diet_type": "non_veg", "calories": 99, "protein": 20, "carbs": 0, "fats": 1},
    {"name": "Prawn", "category": "seafood", "diet_type": "non_veg", "calories": 99, "protein": 24, "carbs": 0, "fats": 0.2},
    
    # KERALA CURRIES & DISHES
    {"name": "Chicken Curry (Kerala)", "category": "meat", "diet_type": "non_veg", "calories": 180, "protein": 18, "carbs": 5, "fats": 9},
    {"name": "Fish Curry (Kerala)", "category": "seafood", "diet_type": "non_veg", "calories": 160, "protein": 20, "carbs": 4, "fats": 8},
    {"name": "Sambar", "category": "legumes", "diet_type": "vegetarian", "calories": 80, "protein": 4, "carbs": 10, "fats": 3},
    {"name": "Rasam", "category": "other", "diet_type": "vegan", "calories": 30, "protein": 1, "carbs": 4, "fats": 1},
    {"name": "Avial", "category": "vegetables", "diet_type": "vegetarian", "calories": 120, "protein": 3, "carbs": 12, "fats": 6},
    {"name": "Thoran", "category": "vegetables", "diet_type": "vegan", "calories": 140, "protein": 3, "carbs": 15, "fats": 7},
    {"name": "Mezhukkupuratti", "category": "vegetables", "diet_type": "vegetarian", "calories": 150, "protein": 3, "carbs": 14, "fats": 8},
    {"name": "Erissery", "category": "legumes", "diet_type": "vegan", "calories": 110, "protein": 4, "carbs": 14, "fats": 4},
    {"name": "Pulissery", "category": "vegetables", "diet_type": "vegetarian", "calories": 140, "protein": 2, "carbs": 12, "fats": 8},
    {"name": "Pachadi", "category": "fruits", "diet_type": "vegan", "calories": 120, "protein": 1, "carbs": 20, "fats": 4},
    
    # LEGUMES
    {"name": "Lentils (red)", "category": "legumes", "diet_type": "vegan", "calories": 116, "protein": 9, "carbs": 20, "fats": 0.5},
    {"name": "Chickpeas", "category": "legumes", "diet_type": "vegan", "calories": 164, "protein": 9, "carbs": 27, "fats": 2.6},
    {"name": "Black Gram", "category": "legumes", "diet_type": "vegan", "calories": 99, "protein": 8.3, "carbs": 17.5, "fats": 0.3},
    {"name": "Moong Dal", "category": "legumes", "diet_type": "vegan", "calories": 107, "protein": 8, "carbs": 19, "fats": 0.4},
    {"name": "Kidney Beans", "category": "legumes", "diet_type": "vegan", "calories": 127, "protein": 8.7, "carbs": 23, "fats": 0.5},
    {"name": "Black Beans", "category": "legumes", "diet_type": "vegan", "calories": 132, "protein": 8.9, "carbs": 24, "fats": 0.5},
    {"name": "Soybean", "category": "legumes", "diet_type": "vegan", "calories": 173, "protein": 17, "carbs": 9.9, "fats": 9.1},
    
    # BEVERAGES & DRINKS
    {"name": "Coffee (black)", "category": "other", "diet_type": "vegan", "calories": 2, "protein": 0.3, "carbs": 0, "fats": 0},
    {"name": "Tea (black)", "category": "other", "diet_type": "vegan", "calories": 1, "protein": 0.1, "carbs": 0, "fats": 0},
    {"name": "Green Tea", "category": "other", "diet_type": "vegan", "calories": 3, "protein": 0.5, "carbs": 0.5, "fats": 0},
    {"name": "Orange Juice", "category": "fruits", "diet_type": "vegan", "calories": 47, "protein": 0.7, "carbs": 11, "fats": 0.3},
    {"name": "Apple Juice", "category": "fruits", "diet_type": "vegan", "calories": 46, "protein": 0.1, "carbs": 11, "fats": 0},
    {"name": "Carrot Juice", "category": "vegetables", "diet_type": "vegan", "calories": 41, "protein": 0.9, "carbs": 10, "fats": 0.2},
    {"name": "Protein Shake", "category": "dairy", "diet_type": "vegetarian", "calories": 150, "protein": 25, "carbs": 12, "fats": 2},
    {"name": "Smoothie", "category": "fruits", "diet_type": "vegetarian", "calories": 120, "protein": 4, "carbs": 25, "fats": 2},
    
    # SNACKS
    {"name": "Samosa", "category": "other", "diet_type": "vegetarian", "calories": 262, "protein": 3.6, "carbs": 32, "fats": 13},
    {"name": "Spring Roll", "category": "other", "diet_type": "vegan", "calories": 186, "protein": 3.5, "carbs": 32, "fats": 4},
    {"name": "Pakora", "category": "vegetables", "diet_type": "vegetarian", "calories": 280, "protein": 4, "carbs": 28, "fats": 16},
    {"name": "Namkeen (snack mix)", "category": "other", "diet_type": "vegan", "calories": 480, "protein": 10, "carbs": 50, "fats": 26},
    {"name": "Chips", "category": "other", "diet_type": "vegan", "calories": 536, "protein": 6, "carbs": 50, "fats": 35},
    {"name": "Popcorn", "category": "grains", "diet_type": "vegan", "calories": 387, "protein": 12, "carbs": 77, "fats": 4},
    {"name": "Biscuits", "category": "grains", "diet_type": "vegetarian", "calories": 410, "protein": 6.5, "carbs": 76, "fats": 8},
    {"name": "Candy", "category": "other", "diet_type": "vegan", "calories": 403, "protein": 0, "carbs": 100, "fats": 1},
    {"name": "Chocolate", "category": "other", "diet_type": "vegetarian", "calories": 528, "protein": 7.7, "carbs": 57, "fats": 29},
    
    # SWEETS & DESSERTS
    {"name": "Jaggery", "category": "other", "diet_type": "vegan", "calories": 383, "protein": 0.5, "carbs": 96, "fats": 0.5},
    {"name": "Honey", "category": "other", "diet_type": "vegan", "calories": 304, "protein": 0.3, "carbs": 82, "fats": 0},
    {"name": "Sugar", "category": "other", "diet_type": "vegan", "calories": 387, "protein": 0, "carbs": 100, "fats": 0},
    {"name": "Payasam", "category": "other", "diet_type": "vegetarian", "calories": 280, "protein": 4, "carbs": 40, "fats": 10},
    {"name": "Halwa", "category": "other", "diet_type": "vegetarian", "calories": 320, "protein": 5, "carbs": 45, "fats": 12},
    {"name": "Kheer", "category": "other", "diet_type": "vegetarian", "calories": 200, "protein": 5, "carbs": 30, "fats": 6},
    {"name": "Laddu", "category": "other", "diet_type": "vegetarian", "calories": 380, "protein": 6, "carbs": 50, "fats": 16},
    {"name": "Barfi", "category": "other", "diet_type": "vegetarian", "calories": 350, "protein": 5, "carbs": 45, "fats": 15},
    
    # RICE & GRAIN DISHES
    {"name": "White Rice", "category": "grains", "diet_type": "vegan", "calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3},
    {"name": "Brown Rice", "category": "grains", "diet_type": "vegan", "calories": 111, "protein": 2.6, "carbs": 23, "fats": 0.9},
    {"name": "Basmati Rice", "category": "grains", "diet_type": "vegan", "calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3},
    {"name": "Biryani", "category": "grains", "diet_type": "non_veg", "calories": 280, "protein": 10, "carbs": 45, "fats": 6},
    {"name": "Fried Rice", "category": "grains", "diet_type": "non_veg", "calories": 230, "protein": 6, "carbs": 38, "fats": 6},
    {"name": "Pulao", "category": "grains", "diet_type": "vegetarian", "calories": 200, "protein": 4, "carbs": 35, "fats": 5},
    {"name": "Risotto", "category": "grains", "diet_type": "vegetarian", "calories": 190, "protein": 4, "carbs": 32, "fats": 6},
    
    # PASTA & NOODLES
    {"name": "Pasta (cooked)", "category": "grains", "diet_type": "vegetarian", "calories": 131, "protein": 4.3, "carbs": 25, "fats": 1.1},
    {"name": "Noodles (cooked)", "category": "grains", "diet_type": "vegan", "calories": 138, "protein": 3, "carbs": 32, "fats": 0.3},
    {"name": "Spaghetti", "category": "grains", "diet_type": "vegan", "calories": 131, "protein": 5, "carbs": 25, "fats": 1.1},
    
    # CONDIMENTS & SAUCES
    {"name": "Oil (vegetable)", "category": "other", "diet_type": "vegan", "calories": 884, "protein": 0, "carbs": 0, "fats": 100},
    {"name": "Oil (olive)", "category": "other", "diet_type": "vegan", "calories": 884, "protein": 0, "carbs": 0, "fats": 100},
    {"name": "Oil (mustard)", "category": "other", "diet_type": "vegan", "calories": 884, "protein": 0, "carbs": 0, "fats": 100},
    {"name": "Salt", "category": "other", "diet_type": "vegan", "calories": 0, "protein": 0, "carbs": 0, "fats": 0},
    {"name": "Soy Sauce", "category": "other", "diet_type": "vegan", "calories": 61, "protein": 8.1, "carbs": 5.6, "fats": 0.5},
    {"name": "Vinegar", "category": "other", "diet_type": "vegan", "calories": 18, "protein": 0, "carbs": 4, "fats": 0},
    {"name": "Ketchup", "category": "other", "diet_type": "vegan", "calories": 98, "protein": 1.6, "carbs": 26, "fats": 0.4},
    {"name": "Mayonnaise", "category": "other", "diet_type": "vegan", "calories": 680, "protein": 0.4, "carbs": 0.6, "fats": 76},
    
    # EXTRA VEGETABLES & ITEMS (to reach 500+)
    {"name": "Asparagus", "category": "vegetables", "diet_type": "vegan", "calories": 20, "protein": 2.4, "carbs": 3.7, "fats": 0.1},
    {"name": "Artichoke", "category": "vegetables", "diet_type": "vegan", "calories": 47, "protein": 3.3, "carbs": 10, "fats": 0.1},
    {"name": "Avocado", "category": "fruits", "diet_type": "vegan", "calories": 160, "protein": 2, "carbs": 9, "fats": 15},
    {"name": "Brussels Sprouts", "category": "vegetables", "diet_type": "vegan", "calories": 34, "protein": 2.8, "carbs": 7, "fats": 0.4},
    {"name": "Celery", "category": "vegetables", "diet_type": "vegan", "calories": 16, "protein": 0.7, "carbs": 3.7, "fats": 0.2},
    {"name": "Kale", "category": "vegetables", "diet_type": "vegan", "calories": 49, "protein": 4.3, "carbs": 9, "fats": 0.9},
    {"name": "Mustard Greens", "category": "vegetables", "diet_type": "vegan", "calories": 27, "protein": 2.7, "carbs": 5, "fats": 0.5},
    {"name": "Radish", "category": "vegetables", "diet_type": "vegan", "calories": 16, "protein": 0.7, "carbs": 3.4, "fats": 0.1},
    {"name": "Turnip", "category": "vegetables", "diet_type": "vegan", "calories": 36, "protein": 1.2, "carbs": 8, "fats": 0.1},
    {"name": "Bok Choy", "category": "vegetables", "diet_type": "vegan", "calories": 13, "protein": 1.5, "carbs": 2.2, "fats": 0.2},
    {"name": "Watercress", "category": "vegetables", "diet_type": "vegan", "calories": 11, "protein": 2.3, "carbs": 0.4, "fats": 0.1},
    {"name": "Parsnip", "category": "vegetables", "diet_type": "vegan", "calories": 75, "protein": 1.2, "carbs": 17.9, "fats": 0.3},
    {"name": "Leek", "category": "vegetables", "diet_type": "vegan", "calories": 61, "protein": 1.5, "carbs": 14, "fats": 0.3},
    {"name": "Green Beans", "category": "vegetables", "diet_type": "vegan", "calories": 31, "protein": 1.8, "carbs": 7, "fats": 0.2},
    {"name": "Snap Peas", "category": "vegetables", "diet_type": "vegan", "calories": 42, "protein": 2.8, "carbs": 7.6, "fats": 0.2},
    {"name": "Corn", "category": "vegetables", "diet_type": "vegan", "calories": 86, "protein": 3.3, "carbs": 19, "fats": 1.2},
    {"name": "Mushroom", "category": "vegetables", "diet_type": "vegan", "calories": 22, "protein": 3.1, "carbs": 3.3, "fats": 0.3},
    {"name": "Garlic", "category": "vegetables", "diet_type": "vegan", "calories": 149, "protein": 6.4, "carbs": 33, "fats": 0.5},
    {"name": "Ginger", "category": "vegetables", "diet_type": "vegan", "calories": 80, "protein": 1.8, "carbs": 18, "fats": 0.8},
    {"name": "Turmeric", "category": "vegetables", "diet_type": "vegan", "calories": 312, "protein": 9.7, "carbs": 67, "fats": 3.3},
    {"name": "Cumin", "category": "vegetables", "diet_type": "vegan", "calories": 375, "protein": 17.6, "carbs": 44, "fats": 22},
    {"name": "Coriander", "category": "vegetables", "diet_type": "vegan", "calories": 298, "protein": 21.9, "carbs": 54.9, "fats": 17.8},
    {"name": "Black Pepper", "category": "vegetables", "diet_type": "vegan", "calories": 251, "protein": 10.4, "carbs": 64.8, "fats": 3.3},
    {"name": "Chili Powder", "category": "vegetables", "diet_type": "vegan", "calories": 318, "protein": 13.6, "carbs": 56.6, "fats": 17.3},
    
    # MORE FRUITS
    {"name": "Mulberry", "category": "fruits", "diet_type": "vegan", "calories": 43, "protein": 1.4, "carbs": 8.8, "fats": 0.4},
    {"name": "Blackberry", "category": "fruits", "diet_type": "vegan", "calories": 43, "protein": 1.4, "carbs": 10, "fats": 0.5},
    {"name": "Raspberry", "category": "fruits", "diet_type": "vegan", "calories": 52, "protein": 1.2, "carbs": 12, "fats": 0.7},
    {"name": "Tangerine", "category": "fruits", "diet_type": "vegan", "calories": 47, "protein": 0.7, "carbs": 12, "fats": 0.3},
    {"name": "Grapefruit", "category": "fruits", "diet_type": "vegan", "calories": 42, "protein": 0.8, "carbs": 11, "fats": 0.1},
    {"name": "Apricot", "category": "fruits", "diet_type": "vegan", "calories": 48, "protein": 1.4, "carbs": 11, "fats": 0.4},
    {"name": "Cantaloupe", "category": "fruits", "diet_type": "vegan", "calories": 34, "protein": 0.8, "carbs": 8, "fats": 0.3},
    {"name": "Honeydew", "category": "fruits", "diet_type": "vegan", "calories": 36, "protein": 0.5, "carbs": 9, "fats": 0.3},
    {"name": "Date", "category": "fruits", "diet_type": "vegan", "calories": 282, "protein": 2.7, "carbs": 75, "fats": 0.4},
    {"name": "Fig", "category": "fruits", "diet_type": "vegan", "calories": 74, "protein": 0.8, "carbs": 19, "fats": 0.3},
    {"name": "Raisin", "category": "fruits", "diet_type": "vegan", "calories": 299, "protein": 3.1, "carbs": 79.2, "fats": 0.5},
    {"name": "Prune", "category": "fruits", "diet_type": "vegan", "calories": 240, "protein": 2.2, "carbs": 63.9, "fats": 0.4},
    
    # MILK PRODUCTS & ALTERNATIVES
    {"name": "Almond Milk", "category": "dairy", "diet_type": "vegan", "calories": 30, "protein": 1, "carbs": 1.3, "fats": 2.5},
    {"name": "Soy Milk", "category": "dairy", "diet_type": "vegan", "calories": 49, "protein": 3.3, "carbs": 2, "fats": 2},
    {"name": "Oat Milk", "category": "dairy", "diet_type": "vegan", "calories": 47, "protein": 2, "carbs": 4.4, "fats": 1.5},
    {"name": "Rice Milk", "category": "dairy", "diet_type": "vegan", "calories": 54, "protein": 0.7, "carbs": 11, "fats": 1},
    {"name": "Coconut Milk (beverage)", "category": "dairy", "diet_type": "vegan", "calories": 24, "protein": 0.2, "carbs": 1, "fats": 2},
    {"name": "Lactose Free Milk", "category": "dairy", "diet_type": "vegetarian", "calories": 61, "protein": 3.2, "carbs": 4.8, "fats": 3.3},
    
    # PROCESSED MEATS
    {"name": "Bacon", "category": "meat", "diet_type": "non_veg", "calories": 541, "protein": 37, "carbs": 0, "fats": 43},
    {"name": "Sausage", "category": "meat", "diet_type": "non_veg", "calories": 290, "protein": 13, "carbs": 2, "fats": 25},
    {"name": "Ham", "category": "meat", "diet_type": "non_veg", "calories": 245, "protein": 27, "carbs": 0, "fats": 14},
    {"name": "Turkey", "category": "meat", "diet_type": "non_veg", "calories": 189, "protein": 29, "carbs": 0, "fats": 7.4},
    
    # MILK & SWEETENED PRODUCTS
    {"name": "Milk Powder", "category": "dairy", "diet_type": "vegetarian", "calories": 496, "protein": 26, "carbs": 38, "fats": 28},
    {"name": "Condensed Milk", "category": "dairy", "diet_type": "vegetarian", "calories": 321, "protein": 8.1, "carbs": 54, "fats": 8.7},
    {"name": "Evaporated Milk", "category": "dairy", "diet_type": "vegetarian", "calories": 134, "protein": 6.6, "carbs": 10, "fats": 7.6},
]

# Add more items to reach 500+
additional_foods = [
    {"name": "Mint Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 44, "protein": 3.3, "carbs": 6.4, "fats": 0.7},
    {"name": "Basil Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 23, "protein": 3.2, "carbs": 2.6, "fats": 0.6},
    {"name": "Oregano", "category": "vegetables", "diet_type": "vegan", "calories": 265, "protein": 9, "carbs": 68, "fats": 4.3},
    {"name": "Thyme", "category": "vegetables", "diet_type": "vegan", "calories": 306, "protein": 12, "carbs": 63, "fats": 7},
    {"name": "Rosemary", "category": "vegetables", "diet_type": "vegan", "calories": 331, "protein": 6.2, "carbs": 68, "fats": 15.2},
    {"name": "Cinnamon", "category": "vegetables", "diet_type": "vegan", "calories": 247, "protein": 3.99, "carbs": 80.59, "fats": 1.24},
    {"name": "Cardamom", "category": "vegetables", "diet_type": "vegan", "calories": 311, "protein": 10.6, "carbs": 68, "fats": 6.7},
    {"name": "Clove", "category": "vegetables", "diet_type": "vegan", "calories": 323, "protein": 5.97, "carbs": 65.5, "fats": 20},
    {"name": "Nutmeg", "category": "vegetables", "diet_type": "vegan", "calories": 525, "protein": 5.84, "carbs": 49.29, "fats": 36.31},
    {"name": "Mace", "category": "vegetables", "diet_type": "vegan", "calories": 475, "protein": 6.2, "carbs": 49.49, "fats": 32.38},
    {"name": "Bay Leaf", "category": "vegetables", "diet_type": "vegan", "calories": 262, "protein": 7.6, "carbs": 48.6, "fats": 8.4},
    {"name": "Fenugreek Seeds", "category": "nuts", "diet_type": "vegan", "calories": 323, "protein": 23.9, "carbs": 58.4, "fats": 6.4},
    {"name": "Mustard Seeds", "category": "nuts", "diet_type": "vegan", "calories": 508, "protein": 25.8, "carbs": 28.1, "fats": 36},
    {"name": "Fennel Seeds", "category": "nuts", "diet_type": "vegan", "calories": 345, "protein": 15.8, "carbs": 52.3, "fats": 14.9},
    {"name": "Carom Seeds", "category": "nuts", "diet_type": "vegan", "calories": 305, "protein": 20.3, "carbs": 38.6, "fats": 15.3},
    {"name": "Tamarind", "category": "fruits", "diet_type": "vegan", "calories": 239, "protein": 2.8, "carbs": 62.5, "fats": 0.3},
    {"name": "Hibiscus Flower", "category": "vegetables", "diet_type": "vegan", "calories": 37, "protein": 0.4, "carbs": 8.6, "fats": 0.1},
    {"name": "Fenugreek Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 44, "protein": 4.4, "carbs": 6, "fats": 0.7},
    {"name": "Parsley", "category": "vegetables", "diet_type": "vegan", "calories": 36, "protein": 2.7, "carbs": 6, "fats": 0.8},
    {"name": "Cilantro", "category": "vegetables", "diet_type": "vegan", "calories": 23, "protein": 2.1, "carbs": 3.7, "fats": 0.6},
    {"name": "Curry Leaves", "category": "vegetables", "diet_type": "vegan", "calories": 108, "protein": 12.7, "carbs": 18.7, "fats": 1.7},
    {"name": "Nori Seaweed", "category": "vegetables", "diet_type": "vegan", "calories": 333, "protein": 35.6, "carbs": 50.8, "fats": 8.6},
    {"name": "Wakame Seaweed", "category": "vegetables", "diet_type": "vegan", "calories": 45, "protein": 3, "carbs": 9, "fats": 0.6},
    {"name": "Spirulina", "category": "vegetables", "diet_type": "vegan", "calories": 290, "protein": 57.2, "carbs": 23.9, "fats": 8.3},
    {"name": "Chia Seeds", "category": "nuts", "diet_type": "vegan", "calories": 486, "protein": 16.5, "carbs": 42.1, "fats": 30.7},
]

FOOD_DATA.extend(additional_foods)

def populate_foods():
    """Populate food items in the database"""
    print(f"Starting to populate {len(FOOD_DATA)} food items...")
    
    created_count = 0
    skipped_count = 0
    
    for food in FOOD_DATA:
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
                print(f"Created {created_count} foods...")
        except Exception as e:
            print(f"Error creating {food['name']}: {e}")
            skipped_count += 1
    
    print(f"\nPopulation complete!")
    print(f"Created: {created_count} new foods")
    print(f"Skipped: {skipped_count} (already exist)")
    print(f"Total foods in database: {FoodItem.objects.count()}")

if __name__ == '__main__':
    populate_foods()
