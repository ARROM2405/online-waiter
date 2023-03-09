from django.db import models
from django_intenum import IntEnumField
from enums import OrderPaymentStatus, OrderPreparationSatus


class Order(models.Model):
    payment_status = IntEnumField(enum=OrderPaymentStatus, default=OrderPaymentStatus.NOT_PAID)
    preparation_status = IntEnumField(enum=OrderPreparationSatus, default=OrderPreparationSatus.NEW)
