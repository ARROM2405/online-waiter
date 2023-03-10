from django.db import models
from enumfields import EnumIntegerField

from .enums import DishType, BeverageType
from orders.models import Order


class FoodAndBeverageBase(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ManyToManyField(to=Order)

    class Meta:
        abstract = True


class Dish(FoodAndBeverageBase):
    type = EnumIntegerField(enum=DishType)

    def __str__(self):
        return f"{self.name} - {self.type}"


class Beverage(FoodAndBeverageBase):
    type = EnumIntegerField(enum=BeverageType)
    alcoholic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.type}"
