from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Display all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

# Add student
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})

# Edit student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})

# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list')