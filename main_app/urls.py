from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.task_index, name='task-index'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail' )
]
