from typing import Any
from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from cars.models import car_model,car_purchase
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator 
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if(request.method == "POST"):
        register_form = forms.user_registration_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect("login")
    else:
        register_form = forms.user_registration_form()
    return render(request,"register.html",{'form' : register_form, 'type' : 'Register'})




class user_login_byView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile') 

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Login informtion incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def profile(request):
    purchases = car_purchase.objects.filter(user=request.user)  
    return render(request, "profile.html", {'purchases': purchases}) 


@method_decorator(login_required,name='dispatch')
class edit_profile_byView(UpdateView):
    model = User
    form_class = forms.user_change_data
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)


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




def user_logout(request):
    logout(request)
    return redirect('login')
