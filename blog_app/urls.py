from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/update/', views.update_profile,name = 'update_profile'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_edit, name ='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name ='post_delete'),
    path('test/', TemplateView.as_view(template_name='blog_app/test.html')),

]
