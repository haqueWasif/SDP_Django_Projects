from django.db import models
from brands.models import brand_model
from django.contrib.auth.models import User

# Create your models here.

class car_model(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    brand = models.ForeignKey(brand_model,on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(blank=True, null= True)
    image = models.ImageField(upload_to='cars/media/uploads/', blank = True, null = True)
    
    def __str__(self) -> str:
        return self.name


class car_comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(car_model, on_delete=models.CASCADE, related_name ='comments')

    def __str__(self) -> str:
        return self.name
    
class car_purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField(default=1)
    date_purchased = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(car_model, on_delete=models.CASCADE)