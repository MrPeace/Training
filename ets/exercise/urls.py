from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_list, name='diary_list'),
    path('diary/create/', views.diary_create, name='diary_create'),
    path('diary/create/diary_create_record/', views.diary_create_record, name='diary_create_record'),
    path('diary/create/diary_delete_record/<int:id>', views.dairy_delete_record, name='diary_delete_record'),
    path('diary/create/diary_update/<int:id>', views.diary_update, name='diary_update'),
    path('diary/create/diary_update/diary_update_record/<int:id>', views.diary_create_record, name='diary_update_record'),
    ]
