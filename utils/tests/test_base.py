from django.test import TestCase
from rest_framework.authtoken.models import Token

from staff.models import Waiter, Manager
from staff.tests.factories import ManagerFactory, WaiterFactory


class StaffApiTestBase(TestCase):
    def setUp(self):
        super().setUp()
        self.manager_user = ManagerFactory()
        self.waiter_user = WaiterFactory()

    def _generate_token_for_existing_user(self, staff_user: [Waiter, Manager]) -> None:
        Token.objects.get_or_create(user=staff_user.user)
