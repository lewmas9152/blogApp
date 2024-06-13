from django.contrib import admin
from .models import Post, UserProfile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)



