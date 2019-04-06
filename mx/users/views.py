from django.shortcuts import render

from users.models import Lesson


def index(request):
    users = Lesson.objects.all()
    return render(request, 'index.html', {'users': users})
