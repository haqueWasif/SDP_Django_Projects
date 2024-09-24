from django import forms 
from . models import posts_model

class post_form(forms.ModelForm):
    class Meta:
         model = posts_model
         fields = '__all__'