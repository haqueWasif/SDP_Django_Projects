from django import forms 
from . models import author_model

class author_form(forms.ModelForm):
    class Meta:
         model = author_model
         fields = '__all__'