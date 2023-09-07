from django.shortcuts import render


def profile_view(request):
    return render(request, "social_users/profile.html")