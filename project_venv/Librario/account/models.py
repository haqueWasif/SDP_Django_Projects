from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


# Create your models here.
class user_account(models.Model):
    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    balance = models.DecimalField(default=0, decimal_places=2,max_digits=12)
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)


    def __str__(self) -> str:
        return str(self.user.first_name)