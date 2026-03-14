from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")

        profile.bio = request.POST.get("bio")

        if request.FILES.get("avatar"):
            profile.avatar = request.FILES.get("avatar")

        request.user.save()
        profile.save()

        return redirect("profile")

    return render(request, "accounts/edit_profile.html")