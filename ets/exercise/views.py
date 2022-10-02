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


def dairy_delete_record(request, id):
    d = Diary.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect(reverse('diary_list'))


def diary_update(request, id):
    d = Diary.objects.get(id=id)
    template = loader.get_template('diary_update.html')
    context = {'diary': d}
    return HttpResponse(template.render(context, request))


def diary_update_record(request, row):
    diary_date = request.POST['diary_date']
    diary_weight = request.POST['diary_weight']
    diary_duration = request.POST['diary_duration']
    diary_activity = request.POST['diary_activity']

    diary = Diary.objects.get(id=row)
    diary.diary_date = diary_date
    diary.diary_weight = diary_weight
    diary.diary_duration = diary_duration
    diary.diary_activity = diary_activity
    diary.save()
    return HttpResponseRedirect(reverse('diary_list'))
