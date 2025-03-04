from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Stack
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SocialForm

# Create your views here.
@login_required(login_url='account_login')
def profile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    profile_activities = user_profile.activity_set.all()
    context = {'user_profile': user_profile, 'profile_activities': profile_activities}
    return render(request, 'users/profile.html', context)


@login_required(login_url='account_login')
def edit_profile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    stacks = Stack.objects.all()

    # user_social = Social.objects.get(profile=user_profile)
    
    if user_profile.social_set.all():
        social_form = SocialForm(instance=user_profile)
    else:
        social_form = SocialForm()

    form = ProfileForm(instance=user_profile)

    context = {'user_profile': user_profile, 
               'form': form,
               'stacks': stacks,
               'social_form': social_form}
    return render(request, 'users/edit-profile.html', context)
