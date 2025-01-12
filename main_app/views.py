from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Tag
from .forms import TaskForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


class Home(LoginView):
    template_name = 'home.html'



def about(request):
    return render(request, "about.html")


class TaskList(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    extra_context = {"task_form": TaskForm()}

    # * template_name is useful because by default, Django wil look for a template named task_list.html (following the convention modelname_list.html)
    # ~ Because we are using a more customized template name so we need to specify it

    # *  context_object_name is useful because by default, Django will use the lowercase name of the model (task_list) as the context variable name
    # ~ Because we are using tasks ( a custom name for better clarity), we need to specify it

    # * extra_context - a simple way to add extra context to the template, usually for static value like a form


class TaskDetail(DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        tags_task_doesnt_have = Tag.objects.exclude(id__in=self.object.tags.all().values_list('id'))

        context['tags'] = tags_task_doesnt_have

        return context


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm


class TaskDelete(DeleteView):
    model = Task
    success_url = "/tasks/"

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name', 'color']

class TagDelete(DeleteView):
    model = Tag 
    success_url ='/tags/'

def associate_tag(request, task_id, tag_id):
    task = Task.objects.get(id=task_id)
    tag = Tag.objects.get(id=tag_id)
    task.tags.add(tag)
    return redirect('task-detail', pk=task.id)

def remove_tag(request, task_id, tag_id):
    task = Task.objects.get(id=task_id)
    tag = Tag.objects.get(id=tag_id)
    task.tags.remove(tag)
    return redirect("task-detail", pk=task.id)

    # TODO
    # TODO 2. try-catch block for better error handling
    # TODO stretch: implement MCdatepicker
    # TODO- write more comments on get_context_data ( line 39)


# * form_class - telling Django to use the custom TaskForm defined in forms.py instead of the default
# ~ we use this when we need to customize the form beyond what Django's default form generation can handle
