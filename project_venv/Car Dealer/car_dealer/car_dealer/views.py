from django.shortcuts import render
from cars.models import car_model
from brands.models import brand_model

# Create your views here.

def home(request, category_slug = None):
    data = car_model.objects.all()
    if category_slug is not None:
        car_brand = brand_model.objects.get(slug = category_slug)
        data = car_model.objects.filter(brand = car_brand)
    brands = brand_model.objects.all()
    return render(request,"home.html",{'data' : data,'brands' : brands})
