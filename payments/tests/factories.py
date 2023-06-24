import decimal

import factory
from factory.django import DjangoModelFactory

from orders.tests.factories import OrderFactory
from payments.models import Tip


class TipFactory(DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    amount = decimal.Decimal("5.00")

    class Meta:
        model = Tip
