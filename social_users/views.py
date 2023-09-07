from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        profile = request.user.profile
    return render(request, "social_users/profile.html", {"profile": profile})

@login_required
def profile_edit(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect("profile_view")

    return render(request, "social_users/profile_edit.html", {"form": form})

@login_required
def profile_delete_view(request):
    user = request.user
    
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "Account deleted!")
        return redirect('home_view')
    return render(request, "social_users/profile_delete.html")
