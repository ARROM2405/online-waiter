from django.test import TestCase

from staff.tests.factories import ManagerFactory, WaiterFactory


class StaffApiTestBase(TestCase):
    def setUp(self):
        super().setUp()
        self.manager_user = ManagerFactory()
        self.waiter_user = WaiterFactory()
