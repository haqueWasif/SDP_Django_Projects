from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django import forms
from .models import user_account,user_address


class user_registration_form(UserCreationForm):
    birthdate = forms.DateField( widget=forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField( choices=GENDER_TYPE)
    city = forms.CharField(max_length=100)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    account_type = forms.ChoiceField( choices=ACCOUNT_TYPE)
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name',
                  'email','gender','birthdate','account_type','postal_code','city',
                  'street_address','country']
        
    # form saving
    def save(self,commit = True):
        our_user = super().save(commit = False)
        if commit == True:
            our_user.save()
            gender = self.cleaned_data.get('gender')
            birthdate = self.cleaned_data.get('birthdate')
            account_type = self.cleaned_data.get('account_type')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            country = self.cleaned_data.get('country')

            user_address.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address,
            )
            user_account.objects.create(
                user = our_user,
                gender = gender,
                account_type = account_type,
                birthdate = birthdate,
                account_no = 10000+our_user.id,
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })



class user_update_form(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except user_account.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birthdate'].initial = user_account.birthdate
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            account, created = user_account.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            address, created = user_address.objects.get_or_create(user=user) 

            account.account_type = self.cleaned_data['account_type']
            account.gender = self.cleaned_data['gender']
            account.birthdate = self.cleaned_data['birthdate']
            account.save()

            address.street_address = self.cleaned_data['street_address']
            address.city = self.cleaned_data['city']
            address.postal_code = self.cleaned_data['postal_code']
            address.country = self.cleaned_data['country']
            address.save()

        return user
