from django.db import models
from django.urls import reverse

STATUS = (
    ("U", "Unassigned"), 
    ("IP", "In Progress"), 
    ("S", "Stuck"),
    ("C", "Completed")
    )

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    date= models.DateField()
    duration= models.IntegerField()
    progress=  models.CharField(max_length=2, choices=STATUS, default=STATUS[0][0])
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'task_id': self.id})
    
