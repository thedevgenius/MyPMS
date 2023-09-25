from django.shortcuts import render
from .models import *

# Create your views here.
def Blog(request):
    posts = Post.objects.all().order_by('-date_created')

    data = {
        'posts' : posts
    }
    return render(request, 'blog.html', data)


def BlogDetails(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog-detail.html', {'post':post})