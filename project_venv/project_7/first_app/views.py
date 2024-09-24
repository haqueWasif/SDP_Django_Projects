from django.shortcuts import render
from first_app.forms import student_form

# Create your views here.

def home(request):
    form = student_form()
    
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    
    return render(request, "home.html", {'form': form})
