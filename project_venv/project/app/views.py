from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is app/courses page.")

def about(request):
    return HttpResponse("This is app/about page.")

def home(request):
    return HttpResponse("This is app page.")