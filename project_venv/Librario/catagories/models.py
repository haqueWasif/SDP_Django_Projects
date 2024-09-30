from django.db import models

# Create your models here.

class catagories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
