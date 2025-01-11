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
        
# * forms.py handles the logic, validation, field customization and widgets

# * task_form.html displays the form in the UI - allowing customization of the appearance and layout without affecting the logic behind the form 