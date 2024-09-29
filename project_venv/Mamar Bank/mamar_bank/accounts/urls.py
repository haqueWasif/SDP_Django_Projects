
from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.user_registration_view.as_view(),name='register'),
    path("login/",views.user_login_view.as_view(),name = 'login'),
    path("logout/",views.user_logout,name = 'logout'),
    path("profile/",views.user_update_view.as_view(),name = 'profile'),
    path("pass_change/",views.pass_change,name="pass_change"),
]
