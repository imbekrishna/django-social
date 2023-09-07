from os import name
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
    
    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)
    image = models.FileField(upload_to="icons/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['order']