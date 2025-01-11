from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.TaskList.as_view(), name='task-index'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'), 
    path('tasks/create/', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'), 
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'), 
    
    
]
