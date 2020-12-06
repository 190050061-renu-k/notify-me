from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Instructor


# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((('User'), {'fields': ('is_instructor',)}),)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Instructor)