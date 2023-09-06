from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
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

    def __str__(self) -> str:
        return self.title[:50]