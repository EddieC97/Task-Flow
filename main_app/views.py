from django.shortcuts import render
from django.http import HttpResponse

class Task:
    def __init__(self,name, description, date, duration, progress):
        self.name = name
        self.description = description
        self.date = date,
        self.duration = duration,
        self.progress = progress

tasks = [
    Task(
        "Throw Rubbish", "throw food in the fridge", "11/01/2025", "30mins", "completed"
    ),
    Task(
        "Wash car", "Go to the car wash ", "12/01/2025", "15mins", "unassigned"
    ),
    Task(
        "Cook food", "make rice", "14/01/2025", "20mins", "in progress"
    ),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def task_index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})
# Create your views here.
