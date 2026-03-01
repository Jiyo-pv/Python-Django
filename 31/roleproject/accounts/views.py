from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Registration with role
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)

        return redirect('login')

    return render(request, 'register.html')


# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            profile = Profile.objects.get(user=user)

            if profile.role == "admin":
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


# Admin Dashboard
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# User Dashboard
def user_dashboard(request):
    return render(request, 'user_dashboard.html')