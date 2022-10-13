from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from .models import *


def dashboard(request):
    diarys = Diary.objects.all().order_by('-diary_date')
    context = {'diarys':diarys}
    return render(request, 'exercise/dashboard.html', context)


def diary(request):
    return render(request, 'exercise/diary.html')


def exercise(request):
    exercises = Exercise.objects.all()
    context = {'exercises': exercises}
    return render(request, 'exercise/exercise.html', context)
