from django.contrib import admin

from .models import *

admin.site.register(Diary)
admin.site.register(Exercise)
admin.site.register(Workout)
