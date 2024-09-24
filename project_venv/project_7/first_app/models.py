from django.db import models

# Create your models here.

class student_model(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    fathers_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Name : {self.name}"