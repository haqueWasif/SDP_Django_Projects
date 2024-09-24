from django import forms 
from catagory.models import catagory_model

class catagory_form(forms.ModelForm):
    class Meta:
        model = catagory_model
        fields = '__all__'
        help_texts = {
            'name' : "write your catagory name",
            'task' : "write your task",
        }
