import factory
from factory.django import DjangoModelFactory
import pytest
from django.contrib.auth.models import User

from staff.models import Waiter, Manager


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: f"username_{n}")
    first_name = factory.Sequence(lambda n: f"first_name_{n}")
    last_name = factory.Sequence(lambda n: f"last_name_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@mail.test")
    is_staff = False
    is_active = True

    class Meta:
        model = User


class WaiterFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Waiter


class ManagerFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Manager
