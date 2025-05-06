from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question

def questions_page(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions')  # or render a thank-you message
    else:
        form = QuestionForm()

    questions = Question.objects.filter(answer_text__isnull=False).order_by('-submitted_at')
    return render(request, 'questions/questions.html', {'form': form, 'questions': questions})
