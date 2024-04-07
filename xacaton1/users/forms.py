from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.forms import ModelForm

from .models import *
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'user_type')


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label=_("Пароль:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    username = forms.CharField(label=_("Почта или логин:"), widget=forms.TextInput(attrs={"autofocus": True, "class": "login"}))
