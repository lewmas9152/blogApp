# forms.py
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields =['title','content']