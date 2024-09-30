
from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.user_registration_view.as_view(),name='register'),
    path("login/",views.user_login_view.as_view(),name = 'login'),
    path("logout/",views.user_logout,name = 'logout'),
    path("profile/",views.profile,name="account"),
    path("edit/",views.user_update_view.as_view(),name="edit_account"),
    path("edit/pass_change/",views.pass_change,name="pass_change"),
    path('deposit/', views.deposit_money, name='deposit'),
    

]
