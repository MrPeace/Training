from django.db import models


class Diary(models.Model):
    diary_date = models.DateField(default='django.utils.timezone.now')
    diary_weight = models.DecimalField(max_digits=4, decimal_places=1)
    diary_duration = models.IntegerField(default=0)
    diary_activity = models.CharField(max_length=20)


class Exercise(models.Model):
    exercise_code = models.CharField(max_length=6)
    exercise_name = models.CharField(max_length=20)
    exercise_steps = models.TextField()


class Workout(models.Model):
    weight = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
