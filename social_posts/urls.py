from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('create/', views.post_create_view, name="post_create"),
]
