from django.shortcuts import render,redirect
from . import forms
from . models import car_model,car_comment,car_purchase
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator 
from django.contrib import messages

# Create your views here.

class car_details_byView(DetailView):
    model = car_model
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'car' 

    def post(self, request, *args, **kwargs):
        comment_form = forms.comment_form(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.comment_form()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

@login_required
def buy_car(request, id):
    user = request.user
    car = car_model.objects.get(pk=id)

    if car.quantity > 0:
        purchase = car_purchase(user=user, car=car)
        purchase.save()
        car.quantity -= 1
        car.save()
        messages.success(request, 'Congratulations on your new car!')
    else:
        messages.error(request, 'Oops! The car is out of stock!')

    return redirect('profile')

