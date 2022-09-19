from django.http import HttpResponse
from django.template import loader

from .models import Diary, Exercise, Workout


def index(request):
    d = Diary.objects.all()
    template = loader.get_template('index.html')
    context = {'diary':d}
    return HttpResponse(template.render(context, request))
