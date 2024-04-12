from django.db import models
from users.models import CustomUser

class PickUpPoint(models.Model):
    city = models.CharField(max_length=250, verbose_name="Город")
    address = models.CharField(max_length=500, verbose_name="Адрес")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.city + ', ' + self.address
