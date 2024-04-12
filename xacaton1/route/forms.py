from django import forms
from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class RouteCreateForm(ModelForm):
    class Meta:
        model = Route
        fields = ['path', 'duration', 'price', 'start', 'end', 'type_of_delivery']
        widgets = {
            'path': TextInput(attrs={"class": "field"}),
            'duration': TextInput(attrs={"class": "field"}),
            'price': TextInput(attrs={"class": "field"}),
            'start': Select(attrs={"class": "field"}),
            'end': Select(attrs={"class": "field"}),
            'type_of_delivery': Select(attrs={"class": "field"}),
        }
