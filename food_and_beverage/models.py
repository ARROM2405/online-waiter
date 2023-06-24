from django.db import models
from enumfields import EnumIntegerField
from .enums import DishType, BeverageType


class FoodAndBeverageBase(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    orders = models.ManyToManyField(to="orders.Order", blank=True)
    units_available = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True


class Food(FoodAndBeverageBase):
    type = EnumIntegerField(enum=DishType)

    def __str__(self):
        return f"{self.name} - {self.type}"


class Beverage(FoodAndBeverageBase):
    type = EnumIntegerField(enum=BeverageType)
    alcoholic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.type}"
