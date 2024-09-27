from django import forms 
from . models import car_comment, car_model



class comment_form(forms.ModelForm):
     class Meta:
          model = car_comment
          fields = ['name','email','body']