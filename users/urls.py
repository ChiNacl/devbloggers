from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.profile, name='profile'),
    path('edit-profile/<uuid:pk>', views.edit_profile, name='edit-profile'),
]