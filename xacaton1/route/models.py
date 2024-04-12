from django.db import models
from pick_up_point.models import *


class TypeOfDelivery(models.Model):
    name = models.CharField(max_length=200, verbose_name="Тип доставки")

    def __str__(self):
        return self.name


class Route(models.Model):
    path = models.IntegerField(verbose_name="Путь")
    duration = models.IntegerField(verbose_name="Длительность")
    price = models.IntegerField(verbose_name="Стоимость доставки")
    start = models.ForeignKey(PickUpPoint, on_delete=models.PROTECT, related_name="start", verbose_name="Начальный пункт")
    end = models.ForeignKey(PickUpPoint, on_delete=models.PROTECT, related_name="end", verbose_name="Конечный пункт")
    type_of_delivery = models.ForeignKey(TypeOfDelivery, on_delete=models.PROTECT, verbose_name="Тип перевозки")

    def __str__(self):
        return self.start.city + ' ' + self.start.address + ', ' + self.end.city + ' ' + self.end.address
