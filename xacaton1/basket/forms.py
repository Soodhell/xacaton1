from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class CreateBasket(ModelForm):
    class Meta:
        model = Basket
        fields = ['count', 'product', 'delivery_point_address']


class ChangeBasket(ModelForm):
    class Meta:
        model = Basket
        fields = ['count', 'product', 'accepted']
