# Program 38: Secure Authentication with Password Hashing
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Register user (Password automatically hashed)
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # create_user automatically hashes password
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')
# Login user
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')
# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        hashed_password = request.user.password
        return render(request, 'dashboard.html', {
            'hashed_password': hashed_password
        })
    else:
        return redirect('login')
# Logout
def user_logout(request):
    logout(request)
    return redirect('login')