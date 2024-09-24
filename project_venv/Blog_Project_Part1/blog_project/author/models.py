from django.db import models

# Create your models here.

class author_model(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name
     


