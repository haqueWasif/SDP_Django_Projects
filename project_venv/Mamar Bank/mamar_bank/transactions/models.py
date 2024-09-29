from django.db import models
from accounts.models import user_account # type: ignore
from .constants import TRANSACTION_TYPE

# Create your models here.

class user_transactions(models.Model):
    account = models.ForeignKey(user_account,related_name='transactions',on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve= models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']