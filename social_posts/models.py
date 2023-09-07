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
    
    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title