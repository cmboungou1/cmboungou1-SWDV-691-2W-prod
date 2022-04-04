from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GoalCategory(models.TextChoices):
    SAT = "SAT"
    GPA = "GPA"

class Goal(models.Model):
    goal_id = models.AutoField(auto_created = True, serialize=False, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=GoalCategory.choices)#,default=GoalCategory.GPA)
    completed = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed"]

class Sat(models.Model):
    sat_id = models.AutoField(auto_created = True, serialize=False, primary_key=True)
    goal = models.OneToOneField(Goal,on_delete=models.CASCADE,related_name="sat")
    practice_test_score = models.FloatField()
    private_tutor_time = models.FloatField()
    have_a_strategy = models.BooleanField(default=False)

    def __str__(self):
        return self.category_sat

class Gpa(models.Model):
    gpa_id = models.AutoField(auto_created = True, serialize=False, primary_key=True)
    goal = models.OneToOneField(Goal,on_delete=models.CASCADE,related_name="gpa")
    current_gpa = models.FloatField()
    library_hours = models.FloatField()
    friends_with_high_gpa = models.FloatField()
    office_hours = models.FloatField()

    def __str__(self):
        return self.category_gpa