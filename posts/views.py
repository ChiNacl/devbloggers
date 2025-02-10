from django.shortcuts import render

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
    return render(request, 'posts/daily_activities.html')