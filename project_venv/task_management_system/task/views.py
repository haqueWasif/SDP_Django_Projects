from django.shortcuts import render,redirect
from . import forms
from task.models import task_model

# Create your views here.

def task(request):
    if(request.method == "POST"):
        task_form = forms.task_form(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
    else:
        task_form = forms.task_form()
    return render(request,"task.html",{'form' : task_form})
    

def edit_task(request,id):
    task = task_model.objects.get(pk = id)
    task_form = forms.task_form(instance=task)
    if(request.method == "POST"):
        task_form = forms.task_form(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
    return render(request,"task.html",{'form' : task_form})

def delete_task(request,id):
    task = task_model.objects.get(pk = id)
    task.delete()
    return redirect("homepage")