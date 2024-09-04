from django import forms
from django.core import validators

# forms api 
# Form is the base class from which contactForm inherits

# widgets == field to html input

class contactForm(forms.Form):
    name = forms.CharField(label = "Full Name : ", help_text="Total length must be within 70 characters", required=False, widget = forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'} ))
    
    # file = forms.FileField()
    
    email = forms.EmailField(label = "User Email")

    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()

    age = forms.CharField(widget=forms.NumberInput)

    check = forms.BooleanField()
    
    # birthday = forms.DateField(widget = forms.DateInput(attrs = {'type' : 'date'}))
    # appointment = forms.DateTimeField(widget = forms.DateInput(attrs = {'type' : 'datetime-local'}))

    birthday = forms.CharField(widget = forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.CharField(widget = forms.DateInput(attrs = {'type' : 'datetime-local'}))


    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
    # size = forms.CharField(choices = CHOICES, widget = forms.RadioSelect) 
    # CharField here produces a bug



    MEAL = [('P', 'Pepperoni'), ('M', 'Mushroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Name should be at least 10 characters long.")
#     #     return  valname
    
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Not a valid email")
#     #     return valemail


#     def clean(self):
#         cleaned_data = super().clean()

#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError("Name should be at least 10 characters long.")


#         if '.com' not in valemail:
#             raise forms.ValidationError("Not a valid email")
        


def len_check(val):
    if len(val) < 10:
        raise forms.ValidationError("Value should be at least 10 characters long.")
    
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Name should be at least 10 characters long.')])
    
    text = forms.CharField(validators=[len_check])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='Age must be at max 34'), validators.MinValueValidator(23, message="age must be at least 24") ] )

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='File extension must be of PDF format')])



class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        
        val_name = self.cleaned_data['name']

        if len(val_name) < 15:
            raise forms.ValidationError("Name should be at least 15 characters long.")
        
        
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']

        if val_con_pass != val_pass:
            raise forms.ValidationError("Passwords do not match")
        

       
        
      


