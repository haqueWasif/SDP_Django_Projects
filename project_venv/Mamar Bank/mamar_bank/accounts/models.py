from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE


# Create your models here.
class user_account(models.Model):
    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=15,choices=ACCOUNT_TYPE)
    account_no = models.PositiveIntegerField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, decimal_places=2,max_digits=12)

    def __str__(self) -> str:
        return str(self.account_no)

class user_address(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.city