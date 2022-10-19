from contextlib import redirect_stderr
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from .models import *


def dashboard(request):
    diarys = Diary.objects.all().order_by('-diary_date')[:7]

    walks = Diary.objects.filter(diary_activity='Walk').count()

    rides = Diary.objects.filter(diary_activity='Bike').count()

    lifts = Diary.objects.filter(diary_activity='Lift').count()

    rests = Diary.objects.filter(diary_activity='Rest').count()

    workouts = Workout.objects.all().order_by('-diary__diary_date')[:1]
    context = {'diarys':diarys
    , 'workouts': workouts
    , 'walks':walks
    , 'rides':rides
    , 'lifts':lifts
    , 'rests':rests
    }
    return render(request, 'exercise/dashboard.html', context)


def diary(request):
    return render(request, 'exercise/diary.html')


def exercise(request):
    exercises = Exercise.objects.all()
    context = {'exercises': exercises}
    return render(request, 'exercise/exercise.html', context)
