from django.contrib import admin
from .models import Assignments, Subject, UserManager, User
# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Assignments)
