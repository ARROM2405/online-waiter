import factory
from factory.django import DjangoModelFactory

from orders.models import Order, Table
from staff.tests.factories import WaiterFactory


class TableFactory(DjangoModelFactory):
    number = factory.Sequence(lambda n: n)

    class Meta:
        model = Table


class OrderFactory(DjangoModelFactory):
    table = factory.SubFactory(TableFactory)
    waiter = factory.SubFactory(WaiterFactory)

    class Meta:
        model = Order
