from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class CreateNews(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'price', 'width', 'length', 'height', 'color']

        widgets = {
            'title': TextInput(attrs={"class": "field"}),
            'content': TextInput(attrs={"class": "field"}),
            'price': TextInput(attrs={"class": "field"}),
            'width': TextInput(attrs={"class": "field"}),
            'length': TextInput(attrs={"class": "field"}),
            'height': TextInput(attrs={"class": "field"}),
            'color': TextInput(attrs={"class": "field"}),
        }


class ChangeNews(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'price', 'width', 'length', 'height', 'color']
