from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import user_registration_form,user_update_form
from django.contrib.auth import login,logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.utils.decorators import method_decorator 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.contrib import messages


# Create your views here.

def send_transaction_email(user,  subject, template):
        message = render_to_string(template, {
            'user' : user,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class user_registration_view(FormView):
    template_name = 'user_registration.html'
    success_url = reverse_lazy('register')
    form_class = user_registration_form

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    
class user_login_view(LoginView):
    template_name = 'user_login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    

def user_logout(request):
    logout(request)
    return redirect('home')
    

class user_update_view(View):
    template_name = 'profile.html'

    def get(self, request):
        form = user_update_form(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = user_update_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  
        return render(request, self.template_name, {'form': form})
    

@login_required
def pass_change(request):
    if(request.method == "POST"):
        form = PasswordChangeForm(request.user, data =  request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,"pass_change.html",{'form' : form})
