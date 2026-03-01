# Program 28: Protect View using login_required
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

# Protected View using decorator
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')