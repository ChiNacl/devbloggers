from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def profile(request, pk):
    return render(request, 'users/profile.html')