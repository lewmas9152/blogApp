from django.db import models
from django.utils import timezone
import base64
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images',blank=True,null = True)

    def __str__(self):
        return self.title
    
    def image_base64(self):
        if self.image:
            with self.image.open('rb') as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return ""


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def __str__(self):
        return self.user.username
    
    def avatar_base64(self):
        with self.avatar.open('rb') as avatar_file:
            return base64.b64encode(avatar_file.read()).decode('utf-8')






