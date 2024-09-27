from django import forms 
from . models import categories_model

class category_form(forms.ModelForm):
    class Meta:
         model = categories_model
         fields = '__all__'