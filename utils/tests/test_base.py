from django.test import TestCase
from rest_framework.authtoken.models import Token

from staff.models import Staff
from staff.tests.factories import ManagerFactory, WaiterFactory


class StaffApiTestBase(TestCase):
    def setUp(self):
        super().setUp()
        self.manager_user = ManagerFactory()
        self.waiter_user = WaiterFactory()

    def _generate_token_for_existing_user(self, staff_user: Staff) -> None:
        return Token.objects.get_or_create(user=staff_user.user)[0]
