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
from django.utils import timezone
from django.utils.dateparse import parse_date
from datetime import timedelta


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


def weekly_view(request):

    now_param = request.GET.get("now")
    if now_param:
        selected_date = parse_date(now_param)
    else:
        selected_date = timezone.now().date()

    # * this gets the now query parameter in the URL
    # * if a user just navigated to the page from another page then it will use the timezone.now().date() because the URL will just be http://127.0.0.1:8000/tasks/weeklyview/
    # ~ if a user used the previous Week/ Current Week / or Next Week links then it will be http://127.0.0.1:8000/tasks/weeklyview/?now=2025-01-13 so parse_date will then extract 2025-01-13 into a string then convert it back to date object

    start_of_week = selected_date - timedelta(days=selected_date.weekday())  
    end_of_week = start_of_week + timedelta(days=6) 

    # ~ weekday method is a built-in method of Python
    # * selected_date.weekday() returns an integer representing the day of the week
    # * selected_date.weekday() is used to find out haw many days has passed since the last Monday
    # * values returned by selected_date.weekday() 0: Monday | 1: Tuesday | 2: Wednesday | 3: Thursday |4: Friday | 5: Saturday |6: Sunday

    # ? Example: If selected_date is 2025-01-15 (Wednesday):
    # ? 1. selected_date.weekday() returns 2 (Wednesday).
    # ? 2. Subtract 2 days from selected_date to get start_of_week (Monday): 2025-01-13.
    # ? 3. Add 6 days to start_of_week to get end_of_week (Sunday): 2025-01-19.

    if "previous" in request.GET:
        selected_date -= timedelta(days=7)
        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

    elif "next" in request.GET:
        selected_date += timedelta(days=7)
        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

    elif "current" in request.GET:
        selected_date = timezone.now().date()  
        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

    # * just wanted to calculate this so I can pass it to the html form
    monday = start_of_week
    tuesday = monday + timedelta(days=1)
    wednesday = monday + timedelta(days=2)
    thursday = monday + timedelta(days=3)
    friday = monday + timedelta(days=4)
    saturday = monday + timedelta(days=5)
    sunday = monday + timedelta(days=6)

    # * This just gets tasks for the week based on the start and end of the week
    tasks_for_week = Task.objects.filter(date__gte=start_of_week, date__lte=end_of_week)

    prev_week = (start_of_week - timedelta(weeks=1)).strftime("%Y-%m-%d")
    next_week = (start_of_week + timedelta(weeks=1)).strftime("%Y-%m-%d")
    current_week = timezone.now().date().strftime("%Y-%m-%d")

    # * strftime("%Y-%m-%d") method is used to convert the date into a string so it can be passed into URLs so now the parse_date can work 

    return render(
        request,
        "tasks/weeklyview.html",
        {
            "tasks": tasks_for_week,
            "start_of_week": start_of_week,
            "end_of_week": end_of_week,
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "prev_week": prev_week,
            "next_week": next_week,
            "current_week": current_week,
        },
    )


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
