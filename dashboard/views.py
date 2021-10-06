from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')