from django.db import models
from django.urls import reverse
from users.models import CustomUser
from news.models import *
from route.models import *


class Basket(models.Model):
    count = models.IntegerField(verbose_name="Кол-во(штук)")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    product = models.ForeignKey(News, on_delete=models.PROTECT)
    parried = models.BooleanField(default=False, verbose_name="Отправил")
    accepted = models.BooleanField(default=False, verbose_name="Забрал")
    delivery_point_address = models.ForeignKey(Route, on_delete=models.PROTECT, verbose_name="Маршрут")

    def get_absolute_url(self):
        return reverse('basket_detail', kwargs={'pk': self.pk})