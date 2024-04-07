from django.db import models
from django.urls import reverse
from users.models import CustomUser
from news.models import News

class Basket(models.Model):
    count = models.IntegerField(verbose_name="Кол-во(штук)")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    product = models.ForeignKey(News, on_delete=models.PROTECT)
