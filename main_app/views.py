from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Task
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def task_index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

class TaskCreate(CreateView):
    model = Task
    fields= '__all__'
    
class TaskUpdate(UpdateView):
    model = Task
    fields= '__all__'
