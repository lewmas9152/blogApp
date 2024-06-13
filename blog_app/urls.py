from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('post/<int:id>/',views.post_detail,name='post_detail')
]
