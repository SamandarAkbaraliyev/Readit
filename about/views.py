from django.shortcuts import render
from .models import Feedback


def index(request):
    feedbacks = Feedback.objects.all()
    ctx = {
        'feedbacks': feedbacks
    }
    return render(request, 'readit/about.html', ctx)
