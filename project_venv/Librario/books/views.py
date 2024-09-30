from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . models import books_model,comment_model,borrow_model
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator 
from django.contrib import messages
from account.models import user_account
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives

# Create your views here.

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


class details_byView(DetailView):
    model = books_model
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'books' 

    

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You need to be logged in to post a comment.')
            return redirect('') 
        comment_form = forms.comment_form(data=self.request.POST)
        books = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.books = books
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        books = self.object # books model er object ekhane store korlam
        comments = books.comments.all()
        comment_form = forms.comment_form()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    


@login_required
def book_borrow(request, id):
    # Fetch the book by ID or return a 404 error if it does not exist
    books = get_object_or_404(books_model, pk=id)
    user = request.user
    user_account_instance = user.account  

    if user_account_instance.balance >= books.price:  
        if books.quantity > 0:
            borrow = borrow_model(user=user, books=books)
            borrow.save()  
            books.quantity -= 1  
            books.save() 
            user_account_instance.balance -= books.price  
            user_account_instance.save()  
            messages.success(request, 'Congratulations! The book has been added to your account.')
            
            # Send transaction email
            send_transaction_email(user, id, "Borrowed Message", "book_borrow.html")   
        else:
            messages.error(request, 'Oops! This book is out of stock!')
    else:
        messages.error(request, 'Insufficient balance to borrow this book.')
    
    return redirect('account')  


@login_required
def return_book(request, borrow_id):
    try:
        borrow_record = borrow_model.objects.get(id=borrow_id, user=request.user)
        book = borrow_record.books
        
        user_account_obj = user_account.objects.get(user=request.user)
        user_account_obj.balance += book.price
        user_account_obj.save()

        borrow_record.delete()
        book.quantity += 1  
        book.save() 
        messages.success(request, 'The book has been returned and the balance updated.')

        # Send transaction email
        send_transaction_email(request.user, borrow_id, "Book Return Message", "book_return.html") 
    except borrow_model.DoesNotExist:
        messages.error(request, 'Borrow record not found.')

    return redirect('account')