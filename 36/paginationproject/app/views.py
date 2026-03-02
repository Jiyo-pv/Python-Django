from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator

def student_list(request):

    search = request.GET.get('search')
    students = Student.objects.all()

    # Search
    if search:
        students = students.filter(name__icontains=search)

    # Pagination (5 per page)
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})