from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.forms import ModelForm, TextInput, Select, PasswordInput

from .models import *
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2')

        widgets = {
            'username': TextInput(attrs={"class": "field"}),
            'email': TextInput(attrs={"class": "field"}),
            'first_name': TextInput(attrs={"class": "field"}),
            'last_name': TextInput(attrs={"class": "field"}),
            'user_type': Select(attrs={"class": "field"}),
            'password': PasswordInput(attrs={"class": "field"}),
            'password2': PasswordInput(attrs={"class": "field"}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'user_type')

        widgets = {
            'username': TextInput(attrs={"class": "field"}),
            'first_name': TextInput(attrs={"class": "field"}),
            'last_name': TextInput(attrs={"class": "field"}),
            'password': TextInput(attrs={"class": "field"}),
            'email': TextInput(attrs={"class": "field"}),
            'user_type': Select(attrs={"class": "field"}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label=_("Пароль:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"field"}),
    )

    username = forms.CharField(label=_("Почта или логин:"), widget=forms.TextInput(attrs={"autofocus": True, "class": "field"}))
