# Program 20: Django Hello World
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")