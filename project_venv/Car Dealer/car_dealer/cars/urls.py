
from django.urls import path
from . import views

urlpatterns = [
    path("details/<int:id>/",views.car_details_byView.as_view(),name="details"),
    path('buy/<int:id>/', views.buy_car, name='buy_car'),
]
