from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class UserLogin(models.Model):
    """
    UserLogin model to store user registration data
    """
    name = models.CharField(max_length=255, verbose_name="Name")
    emailid = models.EmailField(unique=True, max_length=255, verbose_name="Email ID")
    password = models.CharField(max_length=255, verbose_name="Password")
    role = models.CharField(max_length=50, default='user', verbose_name="Role")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    
    class Meta:
        db_table = 'userlogin'
        verbose_name = 'User Login'
        verbose_name_plural = 'User Logins'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.emailid})"
    
    def save(self, *args, **kwargs):
        # Hash password before saving if it's not already hashed
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        """Check if the provided password matches the stored hashed password"""
        return check_password(raw_password, self.password)


class Trainer(models.Model):
    """
    Trainer model to store trainer-specific information
    """
    GOAL_CATEGORY_CHOICES = [
        ('weight_gain', 'Weight Gain'),
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('others', 'Others'),
    ]
    
    user = models.OneToOneField(UserLogin, on_delete=models.CASCADE, related_name='trainer_profile')
    mobile = models.CharField(max_length=10, verbose_name="Mobile Number")
    gender = models.CharField(max_length=10, verbose_name="Gender")
    experience = models.IntegerField(verbose_name="Years of Experience")
    specialization = models.CharField(max_length=100, verbose_name="Specialization")
    certification = models.CharField(max_length=255, blank=True, null=True, verbose_name="Certification")
    goal_category = models.CharField(max_length=20, choices=GOAL_CATEGORY_CHOICES, blank=True, null=True, verbose_name="Assigned Goal Category")
    joining_period = models.CharField(max_length=50, verbose_name="Joining Period")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    class Meta:
        db_table = 'trainer'
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.name} - {self.specialization}"


class UserProfile(models.Model):
    """
    UserProfile model to store user's fitness goals and personal information
    """
    GOAL_CHOICES = [
        ('weight_gain', 'Weight Gain'),
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('others', 'Others'),
    ]
    
    MONTH_CHOICES = [
        (1, '1 Month'),
        (2, '2 Months'),
        (3, '3 Months'),
        (6, '6 Months'),
        (8, '8 Months'),
        (12, '1 Year'),
    ]
    
    WORKOUT_TIME_CHOICES = [
        ('morning', '4 AM to 11 AM'),
        ('evening', '4 PM to 11 PM'),
    ]
    
    DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
        ('others', 'Others'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    user = models.OneToOneField(UserLogin, on_delete=models.CASCADE, related_name='profile')
    mobile_number = models.CharField(max_length=10, verbose_name="Mobile Number", default='0000000000')
    age = models.IntegerField(verbose_name="Age")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Gender")
    current_weight = models.FloatField(verbose_name="Current Weight (kg)")
    current_height = models.FloatField(verbose_name="Current Height (cm)")
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, verbose_name="Goal")
    target_weight = models.FloatField(verbose_name="Target Weight (kg)")
    target_months = models.IntegerField(choices=MONTH_CHOICES, verbose_name="Target Months")
    workout_time = models.CharField(max_length=10, choices=WORKOUT_TIME_CHOICES, verbose_name="Workout Time")
    diet_preference = models.CharField(max_length=20, choices=DIET_CHOICES, verbose_name="Diet Preference")
    food_allergies = models.TextField(blank=True, null=True, verbose_name="Food Allergies")
    health_conditions = models.TextField(blank=True, null=True, verbose_name="Health Conditions")
    payment_status = models.BooleanField(default=False, verbose_name="Payment Status")
    payment_amount = models.IntegerField(default=0, verbose_name="Payment Amount")
    payment_method = models.CharField(max_length=20, blank=True, null=True, verbose_name="Payment Method")
    assigned_trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users', verbose_name="Assigned Trainer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"Profile: {self.user.name}"
    
    def calculate_payment_amount(self):
        """Calculate payment amount based on target months"""
        payment_map = {
            1: 399,
            2: 499,
            3: 699,
            6: 1199,
            8: 1599,
            12: 2199,
        }
        return payment_map.get(self.target_months, 0)
    
    def get_remaining_days(self):
        """Calculate remaining days from plan start date"""
        from datetime import timedelta
        from django.utils import timezone
        if self.payment_status and self.updated_at:
            plan_start = self.updated_at
            plan_end = plan_start + timedelta(days=self.target_months * 30)
            remaining = (plan_end - timezone.now()).days
            return max(0, remaining)
        return self.target_months * 30


class Attendance(models.Model):
    """
    Attendance model to track user attendance requests and trainer approvals
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE, related_name='attendances', verbose_name="User")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='user_attendances', verbose_name="Trainer")
    date = models.DateField(verbose_name="Attendance Date")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="Request Date")
    accepted_date = models.DateTimeField(blank=True, null=True, verbose_name="Accepted Date")
    
    class Meta:
        db_table = 'attendance'
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        ordering = ['-date']
        unique_together = ['user', 'date']
    
    def __str__(self):
        return f"{self.user.name} - {self.date} ({self.status})"


class Review(models.Model):
    """
    Review model for users to rate and review their trainers
    """
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE, related_name='reviews', verbose_name="User")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='trainer_reviews', verbose_name="Trainer")
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], verbose_name="Rating")
    review_text = models.TextField(verbose_name="Review")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.name} - {self.trainer.user.name} ({self.rating} stars)"


class FoodItem(models.Model):
    """
    Food items with nutritional information
    """
    FOOD_CATEGORIES = [
        ('dairy', 'Dairy'),
        ('seafood', 'Seafood'),
        ('nuts', 'Nuts'),
        ('eggs', 'Eggs'),
        ('grains', 'Grains'),
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('meat', 'Meat'),
        ('legumes', 'Legumes'),
        ('other', 'Other'),
    ]
    
    DIET_TYPES = [
        ('vegan', 'Vegan'),           # No animal products at all
        ('vegetarian', 'Vegetarian'), # No meat/seafood, but eggs/dairy OK
        ('non_veg', 'Non-Vegetarian'), # All foods
    ]
    
    name = models.CharField(max_length=100, verbose_name="Food Name")
    food_category = models.CharField(max_length=20, choices=FOOD_CATEGORIES, verbose_name="Category")
    diet_type = models.CharField(max_length=20, choices=DIET_TYPES, default='vegan', verbose_name="Diet Type")
    calories = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Calories (per 100g)")
    protein = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Protein (g)")
    carbs = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Carbohydrates (g)")
    fats = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Fats (g)")
    serving_size = models.CharField(max_length=50, default="100g", verbose_name="Serving Size")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    class Meta:
        db_table = 'food_item'
        verbose_name = 'Food Item'
        verbose_name_plural = 'Food Items'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.food_category})"


class DietPlanTemplate(models.Model):
    """
    Pre-made diet plan templates for different goals and calorie ranges
    """
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_building', 'Muscle Building'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Template Name")
    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES, verbose_name="Goal Type")
    calorie_min = models.IntegerField(verbose_name="Minimum Calories")
    calorie_max = models.IntegerField(verbose_name="Maximum Calories")
    description = models.TextField(blank=True, verbose_name="Description")
    meals_data = models.JSONField(verbose_name="Meals Data")  # {"breakfast": [...], "lunch": [...], "dinner": [...], "snacks": [...]}
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = 'diet_plan_template'
        verbose_name = 'Diet Plan Template'
        verbose_name_plural = 'Diet Plan Templates'
        ordering = ['goal_type', 'calorie_min']
    
    def __str__(self):
        return f"{self.name} ({self.calorie_min}-{self.calorie_max} cal)"


class UserDietPlan(models.Model):
    """
    Personalized diet plan assigned by trainer to user
    """
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE, related_name='diet_plans', verbose_name="User")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='created_diet_plans', verbose_name="Trainer")
    template = models.ForeignKey(DietPlanTemplate, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Template Used")
    plan_name = models.CharField(max_length=100, verbose_name="Plan Name")
    target_calories = models.IntegerField(verbose_name="Target Daily Calories")
    meals_data = models.JSONField(verbose_name="Customized Meals")  # Trainer can modify template
    notes = models.TextField(blank=True, verbose_name="Trainer Notes")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = 'user_diet_plan'
        verbose_name = 'User Diet Plan'
        verbose_name_plural = 'User Diet Plans'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.name} - {self.plan_name}"
