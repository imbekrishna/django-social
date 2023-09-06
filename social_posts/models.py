from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        primary_key=True,
        max_length=100,
        default=True,
        unique=True,
        editable=False,
    )
