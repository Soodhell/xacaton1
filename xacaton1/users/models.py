from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class UserType(models.Model):
    name = models.CharField(max_length=250)

class CustomUser(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT, verbose_name="Вид деятельности: ", null=True)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})