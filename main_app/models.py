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
        return reverse('task-detail', kwargs={'pk': self.id})

    # * we are changing task_id to pk in the get_absolute_url because pk is Django's default parameter name for the primary key in URL patterns
    # ~ Django's class-based views and URL routing expect 'pk' by default
    # ~ using 'pk' ensures consistency with Django's conventions and avoids unnecessary complexity

COLOR_CHOICES = (
    ("White", "#FFFFFF"),
    ("Red", "#FF5733"),
    ("Orange", "#FF8C00"),
    ("Yellow", "#FFD700"),
    ("Green", "#4CAF50"),
    ("Blue", "#2196F3"),
    ("Purple", "#9C27B0"),
    ("Pink", "#E91E63"),
    ("Cyan", "#00BCD4"),
    ("Indigo", "#3F51B5"),
    ("Lime", "#FFEB3B"),
)

class Tag(models.Model):
    name=models.CharField(max_length=50)
    color= models.CharField(max_length=8, choices=COLOR_CHOICES, default=COLOR_CHOICES[0][0])
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={"pk": self.id})
