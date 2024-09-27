from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login_byView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", views.profile, name="profile"),
    path("edit/", views.edit_profile_byView.as_view(), name="edit_profile"),
    path("edit/pass_change/", views.pass_change, name="pass_change"),
]
