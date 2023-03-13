from django.db import models
from django_intenum import IntEnumField

from .enums import DishType, BeverageType
from orders.models import Order


class Dish(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField()
    type = IntEnumField(enum=DishType)
    order = models.ForeignKey(to=Order, null=True, on_delete=models.PROTECT)


class Beverage(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField()
    type = IntEnumField(enum=BeverageType)
    alcoholic = models.BooleanField(default=False)
    order = models.ForeignKey(to=Order, null=True, on_delete=models.PROTECT)
