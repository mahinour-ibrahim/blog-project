from django.shortcuts import render
from .models import Post   

def home(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(request, 'home.html', {"posts": posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')