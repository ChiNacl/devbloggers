from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from posts.models import Activity
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account_login')
def profile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    profile_activities = user_profile.activity_set.all()
    context = {'user_profile': user_profile, 'profile_activities': profile_activities}
    return render(request, 'users/profile.html', context)


@login_required(login_url='account_login')
def edit_profile(request, pk):
    return render(request, 'users/edit-profile.html')
