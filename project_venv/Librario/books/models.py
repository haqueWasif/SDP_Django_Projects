from django.db import models
from catagories.models import catagories
from django.contrib.auth.models import User

# Create your models here.

class books_model(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    catagories = models.ForeignKey(catagories,on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='books/media/uploads/', blank = True, null = True)
    quantity = models.PositiveIntegerField(blank=True, null= True)
    def __str__(self) -> str:
        return self.name


class comment_model(models.Model):
    books = models.ForeignKey(books_model, on_delete=models.CASCADE, related_name ='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class borrow_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(books_model, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)