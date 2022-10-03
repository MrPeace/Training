from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader


def dashboard(request):
    return render(request, 'exercise/dashboard.html')


def diary(request):
    return render(request, 'exercise/diary.html')


def exercise(request):
    return render(request, 'exercise/exercise.html')
