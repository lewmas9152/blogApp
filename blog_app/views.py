from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, PostForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponseForbidden
from django .contrib.auth.models import User
from .models import Post


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'blog_app/profile.html', {'user':user})


@login_required
def update_profile(request,username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        user = get_object_or_404(User, username=username)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', username = request.user.username)
        
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        user = get_object_or_404(User, username=username)
    
    return render(request, 'blog_app/update_profile.html', {
        'user_form': user_form,
        'profile_form':profile_form,
        'user':user
    })
@login_required
def home(request):
    posts = Post.objects.select_related('author__userprofile').all().order_by('-date_posted')
    context = {
        "posts": posts
    }
    return render(request, 'blog_app/home.html', context)


@login_required
def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    context = {
        "post":post
    }
    return render(request,'blog_app/detail.html',context)

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog_app/post_form.html', {'form': form})
@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/post_form.html',{'form': form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'blog_app/post_confirm_delete.html', {'post': post})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login') 