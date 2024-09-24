from django import forms 
from first_app.models import student_model

class student_form(forms.ModelForm):
    class Meta:
        model = student_model 
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student roll',
        }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "write your full name"
        }
        
    