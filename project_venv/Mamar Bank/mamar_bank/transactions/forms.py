
from .models import user_transactions
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import user_account # type: ignore

class transactions_form(forms.ModelForm):
    class Meta:
        model = user_transactions
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()

class depositForm(transactions_form):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class withdrawForm(transactions_form):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount



class loanRequestForm(transactions_form):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount



class TransferForm(forms.ModelForm):
    recipient = forms.CharField()  
    
    class Meta:
        model = user_transactions
        fields = ['amount', 'recipient']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')  # sender's account
        super().__init__(*args, **kwargs)

    def clean_recipient(self):
        recipient_username = self.cleaned_data.get('recipient')
        try:
            recipient_account = user_account.objects.get(user__username=recipient_username)  
        except user_account.DoesNotExist:
            raise ValidationError('The recipient account does not exist.')
        
        return recipient_account  # return the account object if found

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount > self.account.balance:
            raise ValidationError('You cannot transfer more than your account balance.')
        if amount <= 0:
            raise ValidationError('Transfer amount must be greater than 0.')
        
        return amount

    def save(self, commit=True):
        # Deduct the amount from the sender and add to the recipient
        recipient_account = self.cleaned_data.get('recipient')
        amount = self.cleaned_data.get('amount')
        
        self.account.balance -= amount
        recipient_account.balance += amount
        
        if commit:
            self.account.save(update_fields=['balance'])
            recipient_account.save(update_fields=['balance'])
            
        transaction = super().save(commit=False)
        transaction.account = self.account  # this will be the sender's account
        transaction.balance_after_transaction = self.account.balance
        transaction.save()
        
        # Create a new transaction for the recipient
        user_transactions.objects.create(
            account=recipient_account,
            amount=amount,
            balance_after_transaction=recipient_account.balance,
            transaction_type=4  # assuming 4 represents a "transfer" transaction type
        )
        return transaction