from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        primary_key=True,
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    tags = models.ManyToManyField("Tag")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
    )

    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title


class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.post.title}"


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)
    image = models.FileField(upload_to="icons/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["order"]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    parent_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self) -> str:
        try:
            return f"{self.author.username} : {self.body[:30]}"
        except Exception:
            return f"[deleted]: {self.body[:30]}"

    class Meta:
        ordering = ["-created"]


class Reply(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="replies"
    )
    parent_comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies"
    )
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self) -> str:
        try:
            return f"{self.author.username} : {self.body[:30]}"
        except Exception:
            return f"[deleted]: {self.body[:30]}"

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Replies"
