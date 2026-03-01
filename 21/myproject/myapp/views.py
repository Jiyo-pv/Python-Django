# Program 26: Dynamic URL Routing
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.http import HttpResponse
from .models import Student

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return HttpResponse(
        f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}"
    )