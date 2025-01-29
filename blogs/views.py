from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogs(request):
    return render(request, 'blogs/blogs.html')

def blog(request):
    return render(request, 'blogs/blog_detail.html')

def rooms(request):
    return render(request, 'blogs/rooms.html')

def room(request):
    return render(request, 'blogs/room.html')