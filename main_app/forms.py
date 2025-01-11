from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['name', 'description', 'date', 'duration', 'progress']
        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }