from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Diary, Exercise, Workout


def diary_list(request):
    d = Diary.objects.all()
    template = loader.get_template('diary_list.html')
    context = {'diary': d}
    return HttpResponse(template.render(context, request))


def diary_create(request):
    template = loader.get_template('diary_create.html')
    return HttpResponse(template.render({}, request))


def diary_create_record(request):
    x = request.POST['diary_date']
    w = request.POST['diary_weight']
    y = request.POST['diary_duration']
    z = request.POST['diary_activity']
    diary = Diary(diary_date=x, diary_weight=w, diary_duration=y, diary_activity=z)
    diary.save()
    return HttpResponseRedirect(reverse('diary_list'))
