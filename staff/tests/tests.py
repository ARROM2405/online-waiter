from utils.tests.test_base import StaffApiTestBase


# TODO: Test testclass. To be removed.
class TestOrderViewSet(StaffApiTestBase):
    def test_sample(self):
        print(f"Manager: {self.manager_user}")
        print(f"Waiter: {self.waiter_user}")
        assert 1 == 0
