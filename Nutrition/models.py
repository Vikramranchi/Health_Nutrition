

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return self.name

class NutritionPlan(models.Model):
    user_name = models.CharField(max_length=100)
    daily_calories = models.FloatField()
    goal = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.goal}'
