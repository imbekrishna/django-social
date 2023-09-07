from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile_view(request):
    profile = request.user.profile
    return render(request, "social_users/profile.html", {"profile": profile})

def profile_edit(request):
    return render(request, 'social_users/profile_edit.html')