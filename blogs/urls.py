from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/', views.room, name='room'),
]