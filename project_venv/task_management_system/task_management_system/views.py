from django.shortcuts import render 
from task.models import task_model

def home(request):
    data = task_model.objects.all()
    return render(request,"home.html",{'data' : data})