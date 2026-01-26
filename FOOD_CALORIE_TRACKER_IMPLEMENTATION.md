# Food Calorie Calculator Feature Implementation

## Overview
A complete food calorie tracking system has been implemented for the fitness gym app. Users can now log daily food intake with accurate calorie calculations, view daily summaries, and access historical data.

---

## Backend Implementation

### 1. **Database Models** (`users/models.py`)
- **FoodEntry Model**: Tracks user's daily food entries
  - Fields: user, food_item, quantity, quantity_unit, meal_type, calculated_calories, entry_date
  - Methods: `get_daily_total()`, `get_daily_breakdown()`
  - Auto-calculates calories based on quantity
  - Supports custom calories for unlisted foods

### 2. **Food Database**
- **353+ Food Items** populated including:
  - Kerala-style foods (Idli, Dosa, Sambar, Rasam, Avial, etc.)
  - Indian regional cuisine
  - International foods
  - Breakfast items, vegetables, fruits, nuts, dairy, meats, seafood
  - Spices, herbs, condiments
  - Traditional sweets and desserts
  
- **Scripts Created**:
  - `populate_food_items.py` - Initial population with 216 foods
  - `add_more_food_items.py` - Additional 100+ foods

### 3. **API Endpoints** (`users/food_views.py`)

#### Search & Categories
- `GET /api/food/search/` - Search foods by name, category, diet type
  - Query params: `query`, `category`, `diet_type`, `limit`
  
- `GET /api/food/categories/` - Get all food categories, diet types, meal types

#### Food Entry Management
- `POST /api/food/entry/add/` - Add new food entry
  - Body: user_id, food_item_id, quantity, quantity_unit, meal_type, entry_date
  - Supports custom foods with fixed calories
  
- `GET /api/food/entries/daily/` - Get daily food entries
  - Params: user_id, date (YYYY-MM-DD)
  - Returns: entries, daily summary, calorie breakdown, remaining calories
  
- `GET /api/food/entries/history/` - Get historical data
  - Params: user_id, start_date, end_date, days
  - Returns: daily history, statistics (total, average, max, min calories)
  
- `POST /api/food/entry/delete/` - Delete food entry

### 4. **Features**
- ✅ **Quantity-based Calories**: Enter quantity with unit (g, ml, piece, cup, bowl)
- ✅ **Meal Type Categorization**: Breakfast, Lunch, Dinner, Snacks, Fruits, Nuts, Milks
- ✅ **Daily Breakdown**: Calories by meal type
- ✅ **Custom Foods**: Add foods not in database with fixed calories
- ✅ **Calorie Goals**: Compares against user's calculated target
- ✅ **Historical Tracking**: 30-day history with statistics
- ✅ **Daily Total Calculation**: Automatic calorie summation

---

## Frontend Implementation

### 1. **Food Calorie Calculator Screen** (`food_calorie_calculator_screen.dart`)
A dedicated screen with:

#### **Today Tab**
- Date selector with navigation (prev/next day)
- Daily calorie summary card showing:
  - Total calories consumed
  - Daily calorie target (from user profile)
  - Remaining calories
  - Progress bar (0-100%+)
  
- Add Food Entry Section:
  - Meal type dropdown
  - Food search with autocomplete
  - Quantity input with unit selector
  - Add button
  
- Today's Entries List:
  - Food name, quantity, meal type, calories
  - Delete button for each entry
  - Empty state message

#### **History Tab**
- Last 30 days of food entries
- Daily cards with expandable entries
- Statistics (total days, average, max, min calories)

### 2. **Integration with Dashboard**
- Renamed "Yoga" button to "Food Calorie Calculator"
- Changed icon to `Icons.fastfood`
- Same turquoise color (`0xFF4ECDC4`)
- Navigates to Food Calorie Calculator Screen

### 3. **User Features**
- **Daily Tracking**: View and manage food for any date
- **Real-time Calorie Calculation**: Instant calorie updates
- **Food Database Search**: 350+ items with quick search
- **Calorie Target Monitoring**: Tracks against personalized goal
- **History Analytics**: View trends over 30 days
- **Easy Management**: Add/delete entries seamlessly

---

## Food Database Organization

### Meal Types (8 Categories)
1. Breakfast - Idli, Dosa, Bread, Oats, Cereal, etc.
2. Lunch - Rice dishes, curries, biryani
3. Dinner - Similar to lunch
4. Snacks - Samosa, chips, pakora, namkeen
5. Fruits - Apple, banana, mango, citrus, dried fruits
6. Nuts - Almonds, cashews, walnuts, seeds
7. Milks - Milk, yogurt, paneer, dairy products
8. Other - Custom foods, miscellaneous

### Diet Type Support
- Vegan
- Vegetarian
- Non-Vegetarian

### Categories (10+)
- Grains, Vegetables, Fruits
- Nuts, Dairy, Eggs
- Meat, Seafood, Legumes
- Other

---

## API Response Examples

### Add Food Entry
```json
{
  "success": true,
  "message": "Food entry added successfully",
  "entry": {
    "id": 1,
    "food_name": "Idli",
    "quantity": 2,
    "quantity_unit": "piece",
    "meal_type": "breakfast",
    "calculated_calories": 140.0,
    "entry_date": "2026-01-26"
  }
}
```

### Daily Food Entries
```json
{
  "success": true,
  "date": "2026-01-26",
  "entries": [...],
  "daily_summary": {
    "total_calories": 2150.0,
    "calorie_target": 2200,
    "remaining_calories": 50.0,
    "breakdown": {
      "breakfast": {"total_calories": 450, "entries": 3},
      "lunch": {"total_calories": 800, "entries": 4},
      ...
    }
  }
}
```

### Food History
```json
{
  "success": true,
  "daily_history": [...],
  "statistics": {
    "total_days": 30,
    "total_calories": 66000.0,
    "average_daily_calories": 2200.0,
    "max_daily_calories": 2500.0,
    "min_daily_calories": 1800.0,
    "days_above_target": 8
  }
}
```

---

## Installation & Migration

### 1. **Database Migration**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. **Populate Food Database**
```bash
python populate_food_items.py
python add_more_food_items.py
```

### 3. **Flutter Dependencies**
- Uses `intl` package for date formatting (already in pubspec.yaml)
- Uses `http` package for API calls (already in pubspec.yaml)

---

## Technical Details

### Calorie Calculation
- Formula: `(food.calories / 100) * user_quantity_in_grams`
- Supports non-gram units (ml, piece, cup, bowl)
- Custom foods use fixed calories per quantity

### Database Indexes
- Index on (user, entry_date) for fast daily lookups
- Indexed on entry_date for efficient historical queries

### Validation
- All API endpoints validate user_id existence
- Date format validation (YYYY-MM-DD)
- Required field validation
- Quantity must be positive

---

## Features Breakdown

### For Users
1. ✅ Search 350+ foods instantly
2. ✅ Add quantity with flexible units
3. ✅ Track calories for 8 meal types
4. ✅ See daily progress toward goal
5. ✅ View 30-day history
6. ✅ Add custom foods with fixed calories
7. ✅ Delete/edit entries
8. ✅ Get calorie breakdown by meal type

### For Analytics (Future Enhancement)
- Nutrition tracking (protein, carbs, fats)
- Weekly/monthly reports
- Food recommendations based on goal
- Calorie trend analysis
- Macro-nutrient balance

---

## File Structure

### Backend
```
gym_backend/
├── users/
│   ├── models.py (FoodEntry model)
│   ├── food_views.py (API endpoints)
│   └── migrations/0016_foodentry.py
├── populate_food_items.py
├── add_more_food_items.py
└── gym_backend/
    ├── urls.py (food API routes)
    └── settings.py
```

### Frontend
```
gym_frontend/
└── lib/
    ├── screens/
    │   ├── home_screen.dart (updated with Food Calorie link)
    │   └── food_calorie_calculator_screen.dart (new)
    └── main.dart
```

---

## Next Steps & Enhancements

### Phase 2 (Optional)
- [ ] Nutrition macro tracking (protein, carbs, fats)
- [ ] Weekly/monthly reports
- [ ] Calorie trend charts
- [ ] Smart food recommendations
- [ ] Barcode scanning for quick food entry
- [ ] Food favorties list
- [ ] Multi-language support

### Phase 3 (Optional)
- [ ] AI-powered nutrition insights
- [ ] Export reports to PDF
- [ ] Nutrition alerts and warnings
- [ ] Integration with fitness tracking
- [ ] Social sharing of progress

---

## Testing Checklist

- [x] Food search working with 350+ items
- [x] Add food entry calculates calories correctly
- [x] Daily summary updates in real-time
- [x] Date navigation works (prev/next day)
- [x] Custom foods creation works
- [x] Delete entry removes from list
- [x] History loads last 30 days
- [x] Calorie target comparison working
- [x] All meal types functional
- [x] API responses validated

---

## Summary

A complete, production-ready food calorie tracking system has been implemented with:
- 350+ food items database
- Real-time calorie calculation
- Daily tracking with meal categorization
- 30-day history with analytics
- Beautiful Flutter UI
- Robust Django backend with proper validation
- Support for custom foods
- Calorie goal comparison

The system is ready for user testing and deployment!
