from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
from django.urls import reverse
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def task_index(request):
    tasks = Task.objects.all()
    task_form = TaskForm()
    return render(request, "tasks/index.html", {"tasks": tasks , 'task_form': task_form})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    
class TaskDelete(DeleteView):
    model = Task
    success_url= '/tasks/'
    
    # TODO 1. implement task_index + task_detail as CBV
    # TODO 2. try-catch block for better error handling
