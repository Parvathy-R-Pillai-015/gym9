# Food Calorie Tracker API Testing Guide

## API Base URL
```
http://127.0.0.1:8000/api/food/
```

---

## 1. Search Foods

### Endpoint
```
GET /api/food/search/
```

### Parameters
- `query` (required): Food name to search
- `category` (optional): Food category (dairy, seafood, nuts, etc.)
- `diet_type` (optional): vegan, vegetarian, non_veg
- `limit` (optional, default: 50): Number of results

### Example Request
```bash
curl "http://127.0.0.1:8000/api/food/search/?query=idli&limit=10"
```

### Response
```json
{
  "success": true,
  "foods": [
    {
      "id": 1,
      "name": "Idli",
      "category": "grains",
      "diet_type": "vegan",
      "calories_per_100g": 70.0,
      "protein": 2.0,
      "carbs": 15.0,
      "fats": 0.5,
      "serving_size": "100g"
    }
  ],
  "total": 1
}
```

---

## 2. Get Food Categories

### Endpoint
```
GET /api/food/categories/
```

### Example Request
```bash
curl "http://127.0.0.1:8000/api/food/categories/"
```

### Response
```json
{
  "success": true,
  "categories": [
    {"value": "dairy", "label": "Dairy"},
    {"value": "seafood", "label": "Seafood"},
    {"value": "nuts", "label": "Nuts"},
    ...
  ],
  "diet_types": [
    {"value": "vegan", "label": "Vegan"},
    {"value": "vegetarian", "label": "Vegetarian"},
    {"value": "non_veg", "label": "Non-Vegetarian"}
  ],
  "meal_types": [
    {"value": "breakfast", "label": "Breakfast"},
    {"value": "lunch", "label": "Lunch"},
    ...
  ]
}
```

---

## 3. Add Food Entry

### Endpoint
```
POST /api/food/entry/add/
```

### Request Body (with existing food)
```json
{
  "user_id": 1,
  "food_item_id": 1,
  "quantity": 2,
  "quantity_unit": "piece",
  "meal_type": "breakfast",
  "entry_date": "2026-01-26"
}
```

### Request Body (with custom food)
```json
{
  "user_id": 1,
  "food_name": "Homemade Sambar",
  "quantity": 100,
  "quantity_unit": "g",
  "meal_type": "lunch",
  "entry_date": "2026-01-26",
  "custom_calories": 80
}
```

### Example cURL
```bash
curl -X POST "http://127.0.0.1:8000/api/food/entry/add/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "food_item_id": 1,
    "quantity": 2,
    "quantity_unit": "piece",
    "meal_type": "breakfast",
    "entry_date": "2026-01-26"
  }'
```

### Response
```json
{
  "success": true,
  "message": "Food entry added successfully",
  "entry": {
    "id": 1,
    "food_name": "Idli",
    "quantity": 2.0,
    "quantity_unit": "piece",
    "meal_type": "breakfast",
    "calculated_calories": 140.0,
    "entry_date": "2026-01-26"
  }
}
```

---

## 4. Get Daily Food Entries

### Endpoint
```
GET /api/food/entries/daily/
```

### Parameters
- `user_id` (required): User ID
- `date` (required): Date in YYYY-MM-DD format

### Example Request
```bash
curl "http://127.0.0.1:8000/api/food/entries/daily/?user_id=1&date=2026-01-26"
```

### Response
```json
{
  "success": true,
  "date": "2026-01-26",
  "entries": [
    {
      "id": 1,
      "food_name": "Idli",
      "category": "grains",
      "quantity": 2.0,
      "quantity_unit": "piece",
      "meal_type": "breakfast",
      "calculated_calories": 140.0,
      "created_at": "2026-01-26 09:30:00"
    }
  ],
  "daily_summary": {
    "total_calories": 2150.0,
    "calorie_target": 2200,
    "remaining_calories": 50.0,
    "breakdown": {
      "breakfast": {
        "total_calories": 450.0,
        "entries": 3
      },
      "lunch": {
        "total_calories": 800.0,
        "entries": 4
      },
      "dinner": {
        "total_calories": 700.0,
        "entries": 3
      },
      "snacks": {
        "total_calories": 200.0,
        "entries": 2
      },
      "fruits": {
        "total_calories": 0.0,
        "entries": 0
      },
      "nuts": {
        "total_calories": 0.0,
        "entries": 0
      },
      "milks": {
        "total_calories": 0.0,
        "entries": 0
      },
      "other": {
        "total_calories": 0.0,
        "entries": 0
      }
    }
  }
}
```

---

## 5. Get Food History

### Endpoint
```
GET /api/food/entries/history/
```

### Parameters
- `user_id` (required): User ID
- `start_date` (optional): Start date in YYYY-MM-DD
- `end_date` (optional): End date in YYYY-MM-DD
- `days` (optional, default: 30): Number of days to retrieve

### Example Request (Last 30 days)
```bash
curl "http://127.0.0.1:8000/api/food/entries/history/?user_id=1"
```

### Example Request (Date range)
```bash
curl "http://127.0.0.1:8000/api/food/entries/history/?user_id=1&start_date=2026-01-01&end_date=2026-01-26"
```

### Response
```json
{
  "success": true,
  "start_date": "2025-12-27",
  "end_date": "2026-01-26",
  "daily_history": [
    {
      "date": "2026-01-26",
      "total_calories": 2150.0,
      "entries": [
        {
          "id": 1,
          "food_name": "Idli",
          "meal_type": "breakfast",
          "quantity": 2,
          "quantity_unit": "piece",
          "calories": 140.0
        }
      ],
      "breakdown": {
        "breakfast": {"total_calories": 450.0, "entries": 3},
        "lunch": {"total_calories": 800.0, "entries": 4}
      }
    }
  ],
  "statistics": {
    "total_days": 30,
    "total_calories": 66000.0,
    "average_daily_calories": 2200.0,
    "max_daily_calories": 2500.0,
    "min_daily_calories": 1800.0,
    "calorie_target": 2200,
    "days_above_target": 8
  }
}
```

---

## 6. Delete Food Entry

### Endpoint
```
POST /api/food/entry/delete/
```

### Request Body
```json
{
  "user_id": 1,
  "entry_id": 1
}
```

### Example cURL
```bash
curl -X POST "http://127.0.0.1:8000/api/food/entry/delete/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "entry_id": 1
  }'
```

### Response
```json
{
  "success": true,
  "message": "Food entry deleted successfully"
}
```

---

## Available Foods (Sample)

### Breakfast Items
- Idli (70 cal/100g)
- Dosa (150 cal/100g)
- Appam (120 cal/100g)
- Paratha (200 cal/100g)
- Bread (79 cal/100g)
- Oats (68 cal/100g)

### Main Foods
- Chicken Curry (180 cal/100g)
- Fish Curry (160 cal/100g)
- Sambar (80 cal/100g)
- Rasam (30 cal/100g)
- Biryani (280 cal/100g)

### Vegetables
- Spinach (23 cal/100g)
- Broccoli (34 cal/100g)
- Carrot (41 cal/100g)
- Tomato (18 cal/100g)
- Onion (40 cal/100g)

### Proteins
- Paneer (265 cal/100g)
- Egg (155 cal/100g)
- Chicken Breast (165 cal/100g)
- Fish (206 cal/100g)
- Tofu (76 cal/100g)

### Nuts & Seeds
- Almonds (579 cal/100g)
- Cashews (553 cal/100g)
- Peanuts (567 cal/100g)
- Sesame Seeds (563 cal/100g)

### Fruits
- Apple (52 cal/100g)
- Banana (89 cal/100g)
- Orange (47 cal/100g)
- Mango (60 cal/100g)
- Guava (68 cal/100g)

---

## Error Responses

### Missing Required Parameter
```json
{
  "success": false,
  "message": "user_id and date parameters are required"
}
```

### User Not Found
```json
{
  "success": false,
  "message": "User not found"
}
```

### Invalid Date Format
```json
{
  "success": false,
  "message": "Invalid date format. Use YYYY-MM-DD"
}
```

### Food Item Not Found
```json
{
  "success": false,
  "message": "Food item not found"
}
```

---

## Testing with Postman

1. Create a new Postman collection
2. Add requests for each endpoint
3. Use the examples above
4. Set environment variables for user_id if needed
5. Test different query parameters

---

## Integration Notes

### Calorie Calculation
- For foods in database: `(food.calories_per_100g / 100) * quantity_in_grams`
- For custom foods: `custom_calories * quantity`
- Units are converted internally (ml, piece, cup, bowl to grams)

### Date Format
- Always use YYYY-MM-DD format
- Example: 2026-01-26

### Meal Types
- breakfast, lunch, dinner, snacks, fruits, nuts, milks, other

### Quantity Units
- g (grams) - default
- ml (milliliters)
- piece (individual item)
- cup (1 cup measurement)
- bowl (1 bowl measurement)

---

## Performance Tips

1. **Search Optimization**
   - Use specific queries (e.g., "chicken" instead of "c")
   - Use category filter to narrow results
   - Results are limited to 50 by default

2. **History Loading**
   - Default loads last 30 days
   - Can reduce with `days` parameter
   - Or use `start_date` and `end_date` for specific range

3. **Database Indexes**
   - (user, entry_date) indexed for daily lookups
   - Food search is optimized with icontains
   - History queries are efficient

---

## Future Enhancements

- [ ] Bulk import of foods via CSV
- [ ] Barcode scanning
- [ ] Nutritional macros (protein, carbs, fats)
- [ ] Weekly/monthly reports
- [ ] Calorie charts and graphs
- [ ] Food recommendations
- [ ] Dietary restrictions filtering
