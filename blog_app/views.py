from django.shortcuts import render
from django.http import HttpResponse
from django .contrib.auth.models import User
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request,'blog_app/home.html',context)

def create(request):
    pass

def edit(request):
    pass

def delete(request):
    pass
