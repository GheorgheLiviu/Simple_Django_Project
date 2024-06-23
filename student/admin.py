from django.contrib import admin
from django.contrib.auth.models import Permission, User

from student.models import Student


# Register your models here.

admin.site.register(Student)
admin.site.register(User)

