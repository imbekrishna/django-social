from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("tags/<slug:tag>/", views.home_view, name="tag_view"),
    path("create/", views.post_create_view, name="post_create"),
    path("delete/<uuid:post_id>/", views.post_delete_view, name="post_delete"),
    path("edit/<uuid:post_id>/", views.post_edit_view, name="post_edit"),
    path("<uuid:post_id>/", views.post_page_view, name="post_view"),
    path("comment/<uuid:post_id>/", views.comment_sent, name="post_comment"),
    path(
        "comment/delete/<uuid:comment_id>/",
        views.comment_delete_view,
        name="comment_delete",
    ),
    path("reply/<uuid:comment_id>/", views.reply_sent, name="post_reply"),
    path(
        "reply/delete/<uuid:reply_id>/",
        views.reply_delete_view,
        name="reply_delete",
    ),
    path("post/like/<uuid:pk>/", views.like_post, name="post_like"),
    path("comment/like/<uuid:pk>/", views.like_comment, name="comment_like"),
    path("reply/like/<uuid:pk>/", views.like_reply, name="reply_like"),
]
