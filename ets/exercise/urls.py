from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_list, name='diary_list'),
    path('diary/create/', views.diary_create, name='diary_create'),
    path('diary/create/diary_create_record/', views.diary_create_record, name='diary_create_record')
    ]
