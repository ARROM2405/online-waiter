from django.db import models
from enumfields import EnumIntegerField

from staff.models import Waiter
from .enums import OrderPaymentStatus, OrderPreparationSatus


class Table(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number}"


class Order(models.Model):
    payment_status = EnumIntegerField(
        enum=OrderPaymentStatus, default=OrderPaymentStatus.NOT_PAID
    )
    preparation_status = EnumIntegerField(
        enum=OrderPreparationSatus, default=OrderPreparationSatus.NEW
    )
    table = models.ForeignKey(to=Table, on_delete=models.PROTECT)
    waiter = models.ForeignKey(to=Waiter, on_delete=models.PROTECT)
