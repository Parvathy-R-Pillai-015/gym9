# Food Calorie Calculator - User Flow Examples

## Scenario 1: User's Morning Routine

### Step 1: User Opens Food Calorie Calculator
- App navigates to FoodCalorieCalculatorScreen
- Today's date is shown: "Monday, Jan 26, 2026"
- Daily calorie summary shows 0 calories (no entries yet)
- "Add Food Entry" section is ready

### Step 2: User Searches for Breakfast Food
```
Action: Type "idli" in food search
API Call: GET /api/food/search/?query=idli&limit=20
Response: Returns "Idli" with 70 cal/100g
```

### Step 3: User Adds Idli to Breakfast
```
Inputs:
- Meal Type: Breakfast
- Food: Idli (70 cal/100g)
- Quantity: 2
- Unit: piece

API Call: POST /api/food/entry/add/
Request Body:
{
  "user_id": 1,
  "food_item_id": 123,
  "quantity": 2,
  "quantity_unit": "piece",
  "meal_type": "breakfast",
  "entry_date": "2026-01-26"
}

Calculation: 70 cal/100g * 2 pieces (assuming 50g per piece) = 70 calories
(Or server-side: 70 * 2 = 140 if treating 100g as the quantity)

Response: Entry created with 140 calories
```

### Step 4: User Adds Coffee
```
Inputs:
- Meal Type: Breakfast
- Food: Coffee (black) - 2 cal/100g
- Quantity: 200
- Unit: ml

API Call: Similar to above, quantity=200, unit=ml
Calculation: 2 * 200 = 400 calories (or 2 for black coffee)
```

### Step 5: User Checks Daily Summary
```
API Call: GET /api/food/entries/daily/?user_id=1&date=2026-01-26

Response:
{
  "total_calories": 140,
  "calorie_target": 2200,
  "remaining_calories": 2060,
  "breakdown": {
    "breakfast": {"total_calories": 140, "entries": 1}
  }
}

UI Display:
- Progress Bar: 6% (140/2200)
- Text: "140 cal / 2200 cal target"
- Remaining: "2060 cal left"
```

---

## Scenario 2: User's Lunch Routine

### Step 1: User Navigates to Same Day
- Time: 12:30 PM
- User taps today's date again or taps "Today" button
- Daily entries show breakfast items
- Progress shows 140 calories

### Step 2: User Adds Lunch Items

#### Item 1: Rice
```
Inputs:
- Meal Type: Lunch
- Food: White Rice
- Quantity: 100
- Unit: g

Calculation: 130 cal/100g * 100g = 130 calories
```

#### Item 2: Chicken Curry
```
Inputs:
- Meal Type: Lunch
- Food: Chicken Curry (Kerala)
- Quantity: 200
- Unit: g

Calculation: 180 cal/100g * 200g = 360 calories
```

#### Item 3: Salad
```
Inputs:
- Meal Type: Lunch
- Food: Green Salad
- Quantity: 100
- Unit: g

Calculation: 50 cal/100g * 100g = 50 calories
```

### Step 3: Updated Summary
```
API Call: GET /api/food/entries/daily/?user_id=1&date=2026-01-26

Response:
{
  "total_calories": 680,  // 140 (breakfast) + 540 (lunch)
  "calorie_target": 2200,
  "remaining_calories": 1520,
  "breakdown": {
    "breakfast": {"total_calories": 140, "entries": 1},
    "lunch": {"total_calories": 540, "entries": 3}
  }
}

UI Display:
- Progress Bar: 31% (680/2200)
- Entries Listed: 4 items with delete buttons
```

---

## Scenario 3: User Adds Custom Food

### User Has Homemade Dish
```
Issue: Homemade dosa with special ingredients not in database
Solution: Add as custom food

Inputs:
- Meal Type: Snacks
- Food Name: "Mom's Special Dosa"
- Quantity: 1
- Unit: piece
- Custom Calories: 200 (user estimates)

API Call: POST /api/food/entry/add/
Request Body:
{
  "user_id": 1,
  "food_name": "Mom's Special Dosa",
  "quantity": 1,
  "quantity_unit": "piece",
  "meal_type": "snacks",
  "entry_date": "2026-01-26",
  "custom_calories": 200
}

Response:
- System creates new FoodItem "Mom's Special Dosa"
- Creates FoodEntry with 200 calories
- Entry appears in daily list
```

---

## Scenario 4: User Reviews Daily History

### User Switches to History Tab
```
API Call: GET /api/food/entries/history/?user_id=1&days=30

Response Structure:
{
  "daily_history": [
    {
      "date": "2026-01-26",
      "total_calories": 2150,
      "entries": [
        {
          "food_name": "Idli",
          "meal_type": "breakfast",
          "quantity": 2,
          "quantity_unit": "piece",
          "calories": 140
        },
        ...
      ]
    },
    {
      "date": "2026-01-25",
      "total_calories": 2300,
      ...
    },
    ...
  ],
  "statistics": {
    "total_days": 30,
    "total_calories": 66000,
    "average_daily_calories": 2200,
    "max_daily_calories": 2500,
    "min_daily_calories": 1800,
    "days_above_target": 8
  }
}
```

### UI Display
- Statistics Card:
  - Average: 2200 cal/day
  - Max: 2500 cal
  - Min: 1800 cal
  - Days above target: 8

- Expandable Daily Cards:
  - 2026-01-26: 2150 cal (click to expand)
    - Idli (breakfast) - 140 cal
    - Rice (lunch) - 130 cal
    - ... more items
  - 2026-01-25: 2300 cal
  - ... older days

---

## Scenario 5: User Deletes Incorrect Entry

### User Added Wrong Item
```
Action: User added 200g banana instead of 100g
Realization: Total calories increased unexpectedly
Solution: Delete the incorrect entry

UI Action: Tap delete button on "Banana" entry

API Call: POST /api/food/entry/delete/
Request Body:
{
  "user_id": 1,
  "entry_id": 42
}

Response:
{
  "success": true,
  "message": "Food entry deleted successfully"
}

UI Update:
- Entry removed from list
- Daily summary recalculated
- Progress bar updates instantly
```

---

## Scenario 6: User Compares Against Goal

### Morning Weigh-in & Goal Setting
```
User Profile:
- Current Weight: 75 kg
- Target Weight: 70 kg
- Timeline: 3 months
- Goal Type: Weight Loss

Calculated Daily Target:
- 75 kg → 70 kg = 5 kg loss in 12 weeks = ~1.2 kg per week
- Safe rate: 0.5-1 kg per week
- Weekly deficit needed: ~3500 cal (500 cal/day)
- Base BMR: 75 kg * 24 = 1800 cal
- Target: 1800 - 500 = 1300 cal/day (but min 1500 for females)
- Adjusted Target: 1500 cal/day
```

### Daily Tracking
```
Day 1:
- Target: 1500 cal
- Consumed: 1480 cal
- Status: 20 cal under (GREEN - on track)

Day 2:
- Target: 1500 cal
- Consumed: 1620 cal
- Status: 120 cal over (YELLOW - slightly over)

Day 3:
- Target: 1500 cal
- Consumed: 2100 cal
- Status: 600 cal over (RED - significantly over)
- System suggests reviewing food choices
```

---

## Scenario 7: Different Meal Types Distribution

### User's Typical Day
```
Breakfast (6-8 AM):
- Idli: 140 cal
- Coffee: 2 cal
- Total: 142 cal (10% of daily)

Mid-Morning Snack (10 AM):
- Banana: 89 cal
- Total: 89 cal

Lunch (12-2 PM):
- Rice: 130 cal
- Chicken Curry: 360 cal
- Salad: 50 cal
- Total: 540 cal (36% of daily)

Afternoon Snack (4 PM):
- Samosa: 262 cal
- Tea with milk: 50 cal
- Total: 312 cal

Dinner (7-9 PM):
- Fish Curry: 320 cal
- Roti: 70 cal
- Vegetables: 80 cal
- Total: 470 cal (31% of daily)

Fruits (evening):
- Apple: 52 cal
- Almonds (handful): 100 cal
- Total: 152 cal

Daily Total: 1705 cal

Breakdown by Meal Type:
- Breakfast: 142 cal
- Lunch: 540 cal
- Dinner: 470 cal
- Snacks: 312 + 89 = 401 cal
- Fruits: 152 cal
```

---

## Scenario 8: Weekly Trend Analysis

### User Reviews Week Performance
```
API Call: GET /api/food/entries/history/?user_id=1&days=7

Week Data:
- Monday: 1800 cal (within 1500 target)
- Tuesday: 2100 cal (over by 600)
- Wednesday: 1200 cal (under by 300)
- Thursday: 1950 cal (over by 450)
- Friday: 1600 cal (over by 100)
- Saturday: 2500 cal (over by 1000) - social event
- Sunday: 1400 cal (under by 100)

Weekly Average: 1936 cal

Analysis:
- 5 days above target
- 2 days below target
- Saturday exceptional (party)
- Overall: 429 cal/day excess average (3003 excess calories for week)

User's Insight:
- Need to control Tuesday, Thursday, Friday portions
- Wednesday was good day - repeat menu
- Weekends tend to be high
```

---

## Scenario 9: Accessing from Dashboard

### User's Daily Routine
```
1. Opens Fitness Gym App
2. Logs in successfully
3. Sees Home Screen with Dashboard
4. Notices "Food Calorie Calculator" button (previously "Yoga")
5. Taps the button
6. Navigates to FoodCalorieCalculatorScreen
7. Today's date loads automatically
8. Starts adding food entries
9. Can go back to home screen or stay in calculator
```

### Button Interaction
```
Button Properties:
- Text: "Food Calorie Calculator"
- Icon: Icons.fastfood (fork and knife)
- Color: Turquoise (0xFF4ECDC4)
- Position: In Quick Actions grid (2nd position)
- Action: Opens FoodCalorieCalculatorScreen with userId, userName
```

---

## API Call Sequence for Complete Day

```
1. User Opens App
   → GET /api/profile/{user_id}/
   (Load user data including calorie target)

2. User Taps Food Calorie Calculator
   → Navigate to FoodCalorieCalculatorScreen

3. Screen Loads Today's Data
   → GET /api/food/entries/daily/?user_id=1&date=today

4. User Searches Food
   → GET /api/food/search/?query=idli

5. User Adds Food
   → POST /api/food/entry/add/

6. Screen Updates Summary
   → GET /api/food/entries/daily/?user_id=1&date=today

7. User Deletes Wrong Entry
   → POST /api/food/entry/delete/

8. Screen Refreshes
   → GET /api/food/entries/daily/?user_id=1&date=today

9. User Switches to History Tab
   → GET /api/food/entries/history/?user_id=1&days=30

10. User Views Past Days
    → API calls from cached data or refresh individual days
```

---

## Real-World Usage Notes

### Best Practices
1. **Add entries immediately after eating** - Better accuracy
2. **Use consistent units** - Helps with tracking
3. **Review weekly** - Spot trends
4. **Update food database** - Add custom foods you eat often
5. **Compare with goal** - Stay motivated

### Common Issues & Solutions
```
Issue: Forgot to add breakfast
Solution: Go to that date and add entry retroactively

Issue: Food portion size unclear
Solution: Use custom food with estimated calories

Issue: Don't know calorie value
Solution: Search similar foods or estimate from meals

Issue: Calorie target seems wrong
Solution: Update profile/goal for recalculation
```

### Tips for Accurate Tracking
1. Use a food scale when possible
2. Standard portions: 1 piece, 1 cup, 1 bowl
3. Measure liquids in ml
4. Weigh grains/flours in grams
5. Use photo references if available

---

## Success Metrics

### User Achieving Weight Loss Goal
```
Day 1:
- Initial: 75 kg
- Target: 1500 cal/day (500 cal deficit)

Week 1:
- Avg daily calories: 1520 cal
- Expected loss: 0.4 kg (1500 cal deficit * 7 days / 7700)
- Actual: 0.5 kg
- Status: ON TRACK

Month 3:
- Total loss: 3.2 kg
- New weight: 71.8 kg
- Still need: 1.8 kg more
- Status: ON TRACK FOR GOAL
```

### System Providing Value
- User has 30-day history
- Can see patterns and trends
- Makes informed food choices
- Achieves fitness goal
- Maintains accountability

