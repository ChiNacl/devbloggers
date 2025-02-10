from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<uuid:pk>', views.blog_detail, name='blog_detail'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<uuid:pk>', views.room, name='room'),
    path('daily-activities/', views.daily_activities, name='daily_activities'),
]