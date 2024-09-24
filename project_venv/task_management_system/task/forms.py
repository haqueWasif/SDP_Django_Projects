from django import forms 
from task.models import task_model

class task_form(forms.ModelForm):
    class Meta:
        model = task_model
        fields = '__all__'
        help_texts = {
            'Title' : "write your task title"
        }
        widgets = {
            'Assign_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # HTML5 date input
                'placeholder': 'YYYY-MM-DD'
            }),
        }
