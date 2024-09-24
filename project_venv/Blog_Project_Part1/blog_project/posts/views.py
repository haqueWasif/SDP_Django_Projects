from django.shortcuts import render,redirect
from . import forms
from . models import posts_model

# Create your views here.

def add_post(request):
    if(request.method == "POST"):
        post_form = forms.post_form(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")
    else:
        post_form = forms.post_form()
    return render(request,"add_post.html",{'form' : post_form})


def edit_post(request,id):
    post = posts_model.objects.get(pk = id)
    post_form = forms.post_form(instance=post)
    if(request.method == "POST"):
        post_form = forms.post_form(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("homepage")
    return render(request,"add_post.html",{'form' : post_form})


def delete_post(request,id):
    post = posts_model.objects.get(pk = id)
    post.delete()
    return redirect("homepage")

