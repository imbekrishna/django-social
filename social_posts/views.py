import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostCreateForm
from .models import Post


# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request, "social_posts/home.html", {"posts": posts})


def post_create_view(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.cleaned_data["url"])
            sourcecode = BeautifulSoup(website.text, "html.parser")

            find_image = sourcecode.select(
                "meta[content^='https://live.staticflickr.com/']"
            )
            image = find_image[0]["content"]

            post.image = image

            find_title = sourcecode.select("h1.photo-title")
            title = find_title[0].text.strip()

            post.title = title

            find_artist = sourcecode.select("a.owner-name")
            artist = find_artist[0].text.strip()

            post.artist = artist

            post.save()
            return redirect("home_view")

    context = {"form": form}
    return render(request, "social_posts/post_create.html", context)


def post_delete_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    

    return render(request, "social_posts/post_delete.html", {"post": post})
