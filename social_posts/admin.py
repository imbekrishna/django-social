from django.contrib import admin

from .models import Post, Reply, Tag, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)