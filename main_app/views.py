from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def task_index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})
