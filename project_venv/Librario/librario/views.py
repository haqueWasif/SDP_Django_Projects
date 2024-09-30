from django.shortcuts import render
from books.models import books_model
from catagories.models import catagories

# Create your views here.

def home(request,catagory_slug = None):
    data = books_model.objects.all()
    if catagory_slug is not None:
        book_catagory = catagories.objects.get(slug = catagory_slug)
        data = books_model.objects.filter(catagories = book_catagory)
    catagory = catagories.objects.all()
    return render(request,"home.html",{'data' : data, 'catagories' : catagory})
