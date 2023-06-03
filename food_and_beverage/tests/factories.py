import factory
from factory.django import DjangoModelFactory
from decimal import Decimal

from food_and_beverage.enums import DishType, BeverageType
from food_and_beverage.models import Food, Beverage


class FoodAndBeverageBaseFactory(DjangoModelFactory):
    description = "Some description"
    price = Decimal("10.00")
    units_available = 10

    class Meta:
        abstract = True


class FoodFactory(FoodAndBeverageBaseFactory):
    name = factory.Sequence(lambda n: f"food_{n}")
    type = DishType.MAIN_DISH

    class Meta:
        model = Food


class BeverageFactory(FoodAndBeverageBaseFactory):
    name = factory.Sequence(lambda n: f"beverage_{n}")
    type = BeverageType.COLD
    price = Decimal("10.00")

    class Meta:
        model = Beverage
