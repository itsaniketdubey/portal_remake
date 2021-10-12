from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from login.forms import UserLoginForm

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
]


