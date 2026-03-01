# Program 35: Session Management
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Set session
def set_session(request):
    request.session['username'] = "Jiyo"
    return HttpResponse("Session Set Successfully")

# Get session
def get_session(request):
    username = request.session.get('username', "No Session Found")
    return HttpResponse(f"Username: {username}")

# Delete session
def delete_session(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponse("Session Deleted")