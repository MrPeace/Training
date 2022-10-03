from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('diary/', views.diary, name='diary'),
    path('exercise/', views.exercise, name='exercise'),
]
