from django.shortcuts import render
from .models import Activity

# Create your views here.
def blogs(request):
    return render(request, 'posts/blogs.html')


def blog_detail(request, pk):
    return render(request, 'posts/blog_detail.html')


def rooms(request):
    return render(request, 'posts/rooms.html')


def room(request, pk):
    return render(request, 'posts/room.html')


def daily_activities(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        activity_post = request.POST['daily_activity']
        Activity.objects.create(profile=user_profile, activity_post=activity_post)
    
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'posts/daily_activities.html', context)