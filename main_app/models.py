from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

COLOR_CHOICES = (
    ("#FFFFFF", "White"),
    ("#FF5733", "Red"),
    ("#FF8C00", "Orange"),
    ("#FFD700", "Yellow"),
    ("#4CAF50", "Green"),
    ("#2196F3", "Blue"),
    ("#9C27B0", "Purple"),
    ("#E91E63", "Pink"),
    ("#00BCD4", "Cyan"),
    ("#3F51B5", "Indigo"),
    ("#FFEB3B", "Lime"),
)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(
        max_length=8, choices=COLOR_CHOICES, default=COLOR_CHOICES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag-detail", kwargs={"pk": self.id})


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
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.id})

    # * we are changing task_id to pk in the get_absolute_url because pk is Django's default parameter name for the primary key in URL patterns
    # ~ Django's class-based views and URL routing expect 'pk' by default
    # ~ using 'pk' ensures consistency with Django's conventions and avoids unnecessary complexity
