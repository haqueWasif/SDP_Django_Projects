from django.db import models
from categories.models import categories_model
from django.contrib.auth.models import User

# Create your models here.

class posts_model(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(categories_model)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
