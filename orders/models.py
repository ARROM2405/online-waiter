from computedfields.models import ComputedFieldsModel, computed
from django.db import models
from django.db.models import Sum
from enumfields import EnumIntegerField

from staff.models import Waiter
from .enums import OrderPaymentStatus, OrderPreparationSatus, OrderingType, TableStatus


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    status = EnumIntegerField(enum=TableStatus, default=TableStatus.FREE)

    def __str__(self):
        return f"Table {self.number}"


class Order(ComputedFieldsModel):
    payment_status = EnumIntegerField(
        enum=OrderPaymentStatus, default=OrderPaymentStatus.NOT_PAID
    )
    preparation_status = EnumIntegerField(
        enum=OrderPreparationSatus, default=OrderPreparationSatus.NEW
    )
    table = models.ForeignKey(to=Table, on_delete=models.PROTECT, related_name="orders")
    waiter = models.OneToOneField(
        to=Waiter,
        on_delete=models.PROTECT,
        related_name="order",
        null=True,
    )
    ordering_type = EnumIntegerField(enum=OrderingType, default=OrderingType.OFFLINE)
    comment = models.TextField(blank=True, null=True)
    submit_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )

    @computed(
        models.DecimalField(
            max_digits=10,
            decimal_places=2,
            null=True,
            blank=True,
        ),
        depends=[("food_set", ["price"])],
    )
    def total_food_price(self):
        if not self.pk:
            return None
        if self.food_set.exists():
            return self.food_set.aggregate(Sum("price"))["price__sum"]
        return None

    @computed(
        models.DecimalField(
            max_digits=10,
            decimal_places=2,
            null=True,
            blank=True,
        )
    )
    def total_beverage_price(self):
        if not self.pk:
            return None
        if self.beverage_set.exists():
            return self.beverage_set.aggregate(Sum("price"))["price__sum"]
        return None
