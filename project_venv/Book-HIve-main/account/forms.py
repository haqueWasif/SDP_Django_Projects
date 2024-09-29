from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
from django import forms
from .models import user_account


class user_registration_form(UserCreationForm):
    birthdate = forms.DateField( widget=forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField( choices=GENDER_TYPE)
    city = forms.CharField(max_length=100)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name',
                  'email','gender','birthdate','postal_code','city',
                  'street_address','country']
        
    # form saving
    def save(self,commit = True):
        our_user = super().save(commit = False)
        if commit == True:
            our_user.save()
            gender = self.cleaned_data.get('gender')
            birthdate = self.cleaned_data.get('birthdate')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            country = self.cleaned_data.get('country')

            user_account.objects.create(
                user = our_user,
                gender = gender,
                birthdate = birthdate,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address,
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class user_update_form(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # jodi user er account thake 
        if self.instance:
            try:
                account = self.instance.account
            except user_account.DoesNotExist:
                account = None

            if account:
                self.fields['gender'].initial = account.gender
                self.fields['birthdate'].initial = account.birthdate
                self.fields['street_address'].initial = account.street_address
                self.fields['city'].initial = account.city
                self.fields['postal_code'].initial = account.postal_code
                self.fields['country'].initial = account.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            account, created = user_account.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            account.gender = self.cleaned_data['gender']
            account.birthdate = self.cleaned_data['birthdate']
            account.street_address = self.cleaned_data['street_address']
            account.city = self.cleaned_data['city']
            account.postal_code = self.cleaned_data['postal_code']
            account.country = self.cleaned_data['country']
            account.save()

        return user
    


class deposit_form(forms.Form):
     amount = forms.DecimalField(decimal_places=2, max_digits=12, min_value=0.01, label="Deposit Amount")
