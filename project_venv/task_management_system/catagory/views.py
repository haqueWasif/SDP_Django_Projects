from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def catagory(request):
    if(request.method == "POST"):
        catagory_form = forms.catagory_form(request.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect("catagory")
    else:
        catagory_form = forms.catagory_form()
    return render(request,"catagory.html",{'form' : catagory_form})