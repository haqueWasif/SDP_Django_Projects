from django.db import models
from author.models import author_model

# Create your models here.

class profiles_model(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    author = models.OneToOneField(author_model, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
    
