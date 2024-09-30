from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import user_registration_form,user_update_form
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from books.models import borrow_model,books_model
from django.contrib.auth import login,logout,update_session_auth_hash
from django.utils.decorators import method_decorator 
from . import forms
from . models import user_account
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.


def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class user_registration_view(FormView):
    template_name = 'user_registration.html'
    success_url = reverse_lazy('login')
    form_class = user_registration_form

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return super().form_valid(form)
    
class user_login_view(LoginView):
    template_name = 'user_login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    
def user_logout(request):
    logout(request)
    return redirect('login')
    


@method_decorator(login_required,name='dispatch')
class user_update_view(View):
    template_name = 'update_profile.html'

    def get(self, request):
        form = user_update_form(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = user_update_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')  
        return render(request, self.template_name, {'form': form})
    

@login_required
def profile(request):
    borrow = borrow_model.objects.filter(user=request.user) 
    data =  user_account.objects.get(user=request.user) 
    user_account_instance = user_account.objects.get(user=request.user)
    current_balance = user_account_instance.balance
    transactions = []

    for record in borrow:
        transaction_data = {
            'id': record.id,
            'book_name': record.books.name,
            'price': record.books.price,
            'borrow_time': record.date_purchased,
            'balance_after_transaction': current_balance - record.books.price,
            'book_id' : record.books.id
        }
        current_balance = transaction_data['balance_after_transaction']
        transactions.append(transaction_data)
    return render(request, "profile.html", {'borrow': borrow,'data' : data, 'transactions': transactions}) 


@login_required
def pass_change(request):
    if(request.method == "POST"):
        form = PasswordChangeForm(request.user, data =  request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect("account")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,"pass_change.html",{'form' : form})





@login_required
def deposit_money(request):
    if request.method == 'POST':
        form = forms.deposit_form(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_account_instance = request.user.account
            user_account_instance.balance += amount  # Update the balance
            user_account_instance.save()  # Save the updated balance
            messages.success(request, f'Deposited {amount} successfully!')
            
             # Send transaction email
            send_transaction_email(request.user, amount, "Deposit Message", "deposit_email.html")   
            
            return redirect('account')  # Redirect to profile or desired page
    else:
        form = forms.deposit_form()

    return render(request, 'deposit.html', {'form': form})