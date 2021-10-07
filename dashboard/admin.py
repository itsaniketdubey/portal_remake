from django.contrib import admin
from .models import Announcements, Assignments, Faculty, Subject, UserManager, User
# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Assignments)
admin.site.register(Faculty)
admin.site.register(Announcements)
