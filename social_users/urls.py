from django.urls import path

from . import views

urlpatterns = [
    path("", views.profile_view, name="profile_view"),
    path("edit/", views.profile_edit, name="profile_edit"),
    path("onboarding/", views.profile_edit, name="profile_onboarding"),
    path("@<str:username>/", views.profile_view, name="user_profile"),
    path("delete/", views.profile_delete_view, name="profile_delete"),
]
