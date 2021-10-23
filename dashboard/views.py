from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
context = {
    'branchname': Branch.objects.all(),
    'assignmentname': Assignments.objects.all(),
    'announcementname': Announcements.objects.all()

}


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def faculty(request):
    return render(request, 'dashboard/faculty.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'dashboard/settings.html')
