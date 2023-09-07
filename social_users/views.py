from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
            profile = request.user.profile
    return render(request, "social_users/profile.html", {"profile": profile})


def profile_edit(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect("profile_view")

    return render(request, "social_users/profile_edit.html", {"form": form})
