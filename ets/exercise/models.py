from unittest.util import _MAX_LENGTH
from django.db import models


class Diary(models.Model):
    diary_date = models.DateField(default='django.utils.timezone.now')
    diary_weight = models.DecimalField(max_digits=4, decimal_places=1)
    diary_duration = models.IntegerField(default=0)
    diary_activity = models.CharField(max_length=20)

    def __str__(self):
        return self.diary_activity  + ' ' + str(self.diary_date)


class Exercise(models.Model):
    exercise_code = models.CharField(max_length=6)
    exercise_name = models.CharField(max_length=20)
    exercise_steps = models.TextField()

    def __str__(self):
        return self.exercise_code


class Workout(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    notes = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.diary.diary_activity  + ' ' + str(self.diary.diary_date)
