from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def signup_redirect_view(request):
    user_profile_id = request.user.profile.id
    return redirect('edit-profile', pk=user_profile_id)

def login_redirect_view(request):
    user_profile_id = request.user.profile.id
    return redirect('profile', pk=user_profile_id)