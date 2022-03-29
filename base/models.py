from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GoalCategory(models.TextChoices):
    SAT = "SAT"
    GPA = "GPA"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=GoalCategory.choices,default=GoalCategory.GPA)
    completed = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed"]

class Sat(models.Model):
    goal = models.OneToOneField(Goal,on_delete=models.CASCADE)
    category_sat = models.CharField(max_length=200,null=False, blank=False)
    practice_test_score = models.IntegerField()
    private_tutor_time = models.IntegerField()
    have_a_strategy = models.BooleanField(default=False)

    def __str__(self):
        return self.category_sat

class Gpa(models.Model):
    goal = models.OneToOneField(Goal,on_delete=models.CASCADE)
    category_gpa = models.CharField(max_length=200,null=False, blank=False)
    current_gpa = models.IntegerField()
    library_hours = models.IntegerField()
    friends_with_high_gpa = models.IntegerField()
    office_hours = models.IntegerField()

    def __str__(self):
        return self.category_gpa