from django.urls import path
from . import views
from django.contrib.auth import views
from login.forms import UserLoginForm

urlpatterns = [
    path('',views.LoginView.as_view(
                template_name = "login/login.html",
                authentication_form = UserLoginForm
            ), name='login'
    ),
]


