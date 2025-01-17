from django.urls import path 
from .import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.TaskList.as_view(), name='task-index'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'), 
    path('tasks/create/', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'), 
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'), 
    path('tasks/weeklyview/', views.weekly_view, name='weekly-view' ),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/', views.TagList.as_view(), name='tag-index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('tasks/<int:task_id>/associate-tag/<int:tag_id>/', views.associate_tag, name='associate-tag'), 
    path('tasks/<int:task_id>/remove-tag/<int:tag_id>/', views.remove_tag, name='remove-tag'),
    path('accounts/signup/', views.signup, name='signup'), 
    
]
