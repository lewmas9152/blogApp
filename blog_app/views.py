from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django .contrib.auth.models import User
from .models import Post


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect target
    else:
        form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect target
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'blog_app/profile.html', {'user':user})

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
