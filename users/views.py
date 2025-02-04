from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def profile(request, pk):
    return render(request, 'users/profile.html')

def edit_profile(request, pk):
    return render(request, 'users/edit-profile.html')
