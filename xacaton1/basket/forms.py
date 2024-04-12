from django import forms
from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class CreateBasket(ModelForm):
    class Meta:
        model = Basket
        fields = ['count', 'product', 'delivery_point_address']
        widgets ={
            'count': TextInput(attrs={"class": "field"}),
            'product': Select(attrs={"class": "field"}),
            'delivery_point_address': Select(attrs={"class": "field"}),
        }


class ChangeBasket(ModelForm):
    class Meta:
        model = Basket
        fields = ['count', 'product', 'accepted']
