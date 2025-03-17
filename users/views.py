from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Stack, Social
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SocialForm
from django.contrib import messages

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
    user_social = Social.objects.get(profile=user_profile)
    # print(user_social)
    
    if user_social:
        social_form = SocialForm(instance=user_social)
    else:
        social_form = SocialForm()
   

    form = ProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        social_form = SocialForm(request.POST, instance=user_social)
        # print(user_social)

        if form.is_valid():
            stack_list = request.POST.getlist('select-stack')
            profile_form = form.save(commit=False)

            new_stack_list = []

            for stack in stack_list:
                stack_obj = Stack.objects.get(name=stack)
                new_stack_list.append(stack_obj.id)

            profile_form.stack.set(new_stack_list)

            social_links_form = social_form.save(commit=False)
            social_links_form.profile = user_profile
            profile_form.save()
            social_links_form.save()
            messages.success(request, 'profile updated successfully')
            return redirect('profile', pk=user_profile.id)

    context = {'user_profile': user_profile, 
               'form': form,
               'stacks': stacks,
               'social_form': social_form
            }
    return render(request, 'users/edit-profile.html', context)
