from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django .contrib.auth.models import User
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request,'blog_app/home.html',context)

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    context = {
        "post":post
    }
    return render(request,'blog_app/detail.html',context)

def create(request):
    pass

def edit(request):
    pass

def delete(request):
    pass
