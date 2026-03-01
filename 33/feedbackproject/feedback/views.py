from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

# Submit feedback
def submit_feedback(request):
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('view_feedback')

    return render(request, 'form.html', {'form': form})


# View all feedback
def view_feedback(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'feedbacks': feedbacks})