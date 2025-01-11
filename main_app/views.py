from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Task Flow Home working </h1>')

def about(request):
    return HttpResponse('<h1> Task Flow About page working </h1>')
    # return render(request, 'about.html')

# Create your views here.
