from django.shortcuts import render,redirect
from . forms import user_register_form,change_user_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.


def home(request):
    return render(request,'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            form = user_register_form(request.POST)
            if form.is_valid():
                messages.success(request,"Account Created Successfully")
                form.save()
                print(form.cleaned_data)
        else : 
            form = user_register_form()
        return render(request,"signup.html",{'form' : form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                # check kortechi user database e ache kina
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # profile page e redirect korbe
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            form = change_user_data(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,"Account Updated Successfully")
                form.save()
                print(form.cleaned_data)
        else : 
            form = change_user_data(instance = request.user)
        return render(request,"profile.html",{'form' : form})
    else:
        return redirect('signup')


def user_logout(request):
    logout(request)
    return redirect('login')



def pass_change(request):
    if request.user.is_authenticated: 
        if request.method == 'POST' : 
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user) # password update korbe
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'pass_change.html',{'form' : form})
    else:
        return redirect('login')



def pass_change2(request):
    if request.user.is_authenticated: 
        if request.method == 'POST' : 
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user) # password update korbe
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'pass_change.html',{'form' : form})
    else:
        return redirect('login')
    

