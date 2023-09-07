import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PostCreateForm, PostEditForm
from .models import Post, Tag


def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()

    categories = Tag.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
        "tag": tag,
    }
    return render(
        request,
        "social_posts/home.html",
        context,
    )

@login_required
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

            post.author = request.user

            post.save()
            form.save_m2m()

            return redirect("home_view")

    context = {"form": form}
    return render(request, "social_posts/post_create.html", context)

@login_required
def post_delete_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted")
        return redirect("home_view")

    return render(
        request,
        "social_posts/post_delete.html",
        {"post": post},
    )

@login_required()
def post_edit_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post, author=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated")
            return redirect("home_view")

    context = {
        "post": post,
        "form": form,
    }
    return render(
        request,
        "social_posts/post_edit.html",
        context,
    )


def post_page_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "social_posts/post_page.html", {"post": post})
