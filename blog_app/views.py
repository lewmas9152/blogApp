from django.shortcuts import render
from django.http import HttpResponse


blogs = [{
    'Title':"My first blog",
    'Author': "IconSam",
    'category':"Technology",
    'content':"I am very happy to be writing my first blog app",

},
{
    'Title':"My Second blog",
    'Author': "Iconicsam",
    'category':"Tech",
    'content':"I am very happy to be writing my first django blogApp",

}]
def home(request):
    context = {
        "blogs": blogs
    }
    return render(request,'blog_app/home.html',context)
