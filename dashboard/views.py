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
        if request.user.is_admin:
            return render(request, 'dashboard/dashboard.html', context)
        elif request.user.is_staff:
            return render(request, 'dashboard/teacher.html', context)


@login_required(login_url='login')
def faculty(request):
    return render(request, 'dashboard/faculty.html')


@login_required(login_url='login')
def ica(request):
    return render(request, 'dashboard/ica.html')


@login_required(login_url='login')
def library(request):
    return render(request, 'dashboard/library.html')


@login_required(login_url='login')
def assignments(request):
    return render(request, 'dashboard/assignments.html')


@login_required(login_url='login')
def timetable(request):
    return render(request, 'dashboard/timetable.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'dashboard/settings.html')


@login_required(login_url='login')
def attendance(request):
    return render(request, 'dashboard/attendance.html')
