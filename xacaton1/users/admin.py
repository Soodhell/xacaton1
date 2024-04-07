from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'password', 'email')

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
