from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account_login')
def profile(request, pk):
    return render(request, 'users/profile.html')


@login_required(login_url='account_login')
def edit_profile(request, pk):
    return render(request, 'users/edit-profile.html')
