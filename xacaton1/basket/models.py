from django.db import models
from django.urls import reverse
from users.models import CustomUser
from news.models import News

class Basket(models.Model):
    count = models.IntegerField(verbose_name="Кол-во(штук)")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    product = models.ForeignKey(News, on_delete=models.PROTECT)
    parried = models.BooleanField(default=False, verbose_name="Отправил")
    accepted = models.BooleanField(default=False, verbose_name="Забрал")
    delivery_point_address = models.CharField(verbose_name="Адрес отправителя", null=True)
    address_of_the_recipient = models.CharField(verbose_name="Адресс получателя", null=True)