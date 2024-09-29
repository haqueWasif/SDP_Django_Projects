
from django.urls import path
from . import views

urlpatterns = [
    path("details/<int:id>/",views.details_byView.as_view(),name="details"),
    path('borrow/<int:id>/', views.book_borrow, name='boorow_book'),
    path("return/<int:borrow_id>/", views.return_book, name='return_book')
]
