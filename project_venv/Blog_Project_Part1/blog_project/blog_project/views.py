from django.shortcuts import render
from posts.models import posts_model

# Create your views here.

def home(request):
    data = posts_model.objects.all()
    return render(request,"home.html",{'data' : data})
