from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Tag
from .forms import TaskForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, "about.html")


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    extra_context = {"task_form": TaskForm()}

    # * template_name is useful because by default, Django wil look for a template named task_list.html (following the convention modelname_list.html)
    # ~ Because we are using a more customized template name so we need to specify it

    # *  context_object_name is useful because by default, Django will use the lowercase name of the model (task_list) as the context variable name
    # ~ Because we are using tasks ( a custom name for better clarity), we need to specify it

    # * extra_context - a simple way to add extra context to the template, usually for static value like a form


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tags_task_doesnt_have = Tag.objects.exclude(id__in=self.object.tags.all().values_list('id')).filter(user=self.request.user)
        
        context['tags'] = tags_task_doesnt_have

        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/tasks/"


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name', 'color']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagList(LoginRequiredMixin, ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'color']

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag 
    success_url ='/tags/'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


@login_required
def associate_tag(request, task_id, tag_id):
    task = Task.objects.get(id=task_id, user=request.user)
    tag = Tag.objects.get(id=tag_id, user=request.user)
    task.tags.add(tag)
    return redirect('task-detail', pk=task.id)


@login_required
def remove_tag(request, task_id, tag_id):
    task = Task.objects.get(id=task_id, user=request.user)
    tag = Tag.objects.get(id=tag_id, user=request.user)
    task.tags.remove(tag)
    return redirect("task-detail", pk=task.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

    # TODO
    # TODO 2. try-catch block for better error handling
    # TODO stretch: implement MCdatepicker


# * form_class - telling Django to use the custom TaskForm defined in forms.py instead of the default
# ~ we use this when we need to customize the form beyond what Django's default form generation can handle

# * get_queryset() is used in ListView to retrieve a collection of objects. It filters, modify or customizes the list of objects that will be passed to the template
# ~ For TaskList, get_queryset() helps filter and return all tasks associated with the current logged-in user
# ! get_queryset() is used to filter multiple objects: like in ListView, DeleteView and UpdateView

# * get_context_data() is used in DetailView to get the data for a single object, plus any additional context that you want to pass to the template
# ~ For TaskDetail, get_context_data adds additional tags to the context, excluding those already associated with the task, and filtering them by the current user
# ? the TaskDetail view automatically retrieves the task object using get_object() that is built in DetailView, then get_context_data() us where you can add extra context for the template
#! get_context_data() is used to add extra information to the context for the template: usually used in DetailView

# & for more info:https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/
