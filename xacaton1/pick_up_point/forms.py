from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *

class CreatePickUpPointForm(LoginRequiredMixin, ModelForm):

    class Meta:
        model = PickUpPoint
        fields = ['city', 'address']