from django.shortcuts import render
from .forms import StudentForm

def register_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return render(request, 'success.html')

    return render(request, 'form.html', {'form': form})