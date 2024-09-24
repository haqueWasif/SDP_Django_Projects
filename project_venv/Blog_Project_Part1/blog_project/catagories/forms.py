from django import forms 
from . models import catagories_model

class catagory_form(forms.ModelForm):
    class Meta:
         model = catagories_model
         fields = '__all__'