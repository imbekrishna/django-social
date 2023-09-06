from django.shortcuts import render

from .models import Post


# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request, "social_posts/home.html", {"posts": posts})

def post_create_view(request):
    """
    docstring
    """
    return render(request, "social_posts/post_create.html")