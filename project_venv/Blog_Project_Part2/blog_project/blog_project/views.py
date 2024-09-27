from django.shortcuts import render
from posts.models import posts_model
from categories.models import catagories_model

# Create your views here.

def home(request, catagory_slug = None):
    data = posts_model.objects.all()
    if catagory_slug is not None:
        post_catagory = catagories_model.objects.get(slug = catagory_slug)
        data = posts_model.objects.filter(catagory = post_catagory)
    catagories = catagories_model.objects.all()
    return render(request,"home.html",{'data' : data, 'catagories' : catagories})
