from ast import arg
from django.http import HttpResponse
from pkg_resources import parse_requirements
import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import CommentCreateForm, PostCreateForm, PostEditForm, ReplyCreateForm
from .models import Comment, Post, Reply, Tag


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

    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()

    if request.htmx:
        if "top" in request.GET:
            # comments = (
            #     post.comments.filter(likes__isnull=False).distinct().order_by("-likes")
            # )
            comments = (
                post.comments.annotate(num_likes=Count("likes"))
                .filter(num_likes__gt=0)
                .order_by("-num_likes")
            )
        else:
            comments = post.comments.all()
        return render(
            request,
            "snippets/loop_postpage_comments.html",
            {
                "comments": comments,
                "replyform": replyform,
            },
        )

    context = {
        "post": post,
        "commentform": commentform,
        "replyform": replyform,
    }

    return render(request, "social_posts/post_page.html", context)


@login_required
def comment_sent(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replyform = ReplyCreateForm()

    if request.method == "POST":
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return render(
        request,
        "snippets/add_comment.html",
        {
            "comment": comment,
            "post": post,
            "replyform": replyform,
        },
    )


@login_required
def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted")
        return redirect("post_view", comment.parent_post.id)

    return render(
        request,
        "social_posts/comment_delete.html",
        {"comment": comment},
    )


@login_required
def reply_sent(request, comment_id):
    parent_comment = get_object_or_404(Comment, id=comment_id)

    replyform = ReplyCreateForm()

    if request.method == "POST":
        form = ReplyCreateForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = parent_comment
            reply.save()

    context = {
        "comment": parent_comment,
        "reply": reply,
        "replyform": replyform,
    }

    return render(
        request,
        "snippets/add_reply.html",
        context,
    )


@login_required
def reply_delete_view(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, author=request.user)

    if request.method == "POST":
        reply.delete()
        messages.success(request, "Reply deleted")
        return redirect("post_view", reply.parent_comment.parent_post.id)

    return render(
        request,
        "social_posts/reply_delete.html",
        {"reply": reply},
    )


def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get("pk"))
            user_exists = post.likes.filter(username=request.user.username).exists()

            if post.author != request.user:
                if user_exists:
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)
            return func(request, post)

        return wrapper

    return inner_func


@login_required
@like_toggle(Post)
def like_post(request, post):
    return render(request, "snippets/likes.html", {"post": post})


@login_required
@like_toggle(Comment)
def like_comment(request, post):
    return render(request, "snippets/likes_comment.html", {"comment": post})


@login_required
@like_toggle(Reply)
def like_reply(request, post):
    return render(request, "snippets/likes_reply.html", {"reply": post})
