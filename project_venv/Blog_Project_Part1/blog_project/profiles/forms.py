from django import forms 
from . models import profiles_model

class profiles_form(forms.ModelForm):
    class Meta:
         model = profiles_model
         fields = '__all__'