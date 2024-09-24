from django.db import models
from catagory.models import catagory_model

# Create your models here.

class task_model(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Assign_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    Catagory = models.ManyToManyField(catagory_model)

    def __str__(self) -> str:
        return self.Title
