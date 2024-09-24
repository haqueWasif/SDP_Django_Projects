from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def add_profile(request):
    if(request.method == "POST"):
        profiles_form = forms.profiles_form(request.POST)
        if profiles_form.is_valid():
            profiles_form.save()
            return redirect("add_profile")
    else:
        profiles_form = forms.profiles_form()
    return render(request,"add_profile.html",{'form' : profiles_form})
