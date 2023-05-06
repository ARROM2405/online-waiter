from rest_framework.reverse import reverse

from utils.tests.test_base import StaffApiTestBase


class TestUserLoginViewSet(StaffApiTestBase):
    def setUp(self):
        super().setUp()
        self.url = reverse("-login")

    def test_login_ok(self):
        response = self.client.post(
            path=self.url,
            data={
                "username": self.manager_user.user.username,
                "password": self.manager_user.user.password,
            },
        )
        response_data = response.data
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.manager_user.id, response_data["user_id"])
        self.assertTrue(response_data["token"])

    def test_login_username_not_exist(self):
        response = self.client.post(
            path=self.url,
            data={
                "username": "incorrect_username",
                "password": self.manager_user.user.password,
            },
        )
        self.assertEqual(401, response.status_code)
        self.assertEqual("User login failed.", response.data["detail"])

    def test_login_incorrect_password(self):
        response = self.client.post(
            path=self.url,
            data={
                "username": self.manager_user.user.username,
                "password": "incorrect_password",
            },
        )
        self.assertEqual(401, response.status_code)
        self.assertEqual("User login failed.", response.data["detail"])

    def test_not_all_credentials_passed(self):
        response = self.client.post(
            path=self.url,
            data={
                "username": self.manager_user.user.username,
                "password": "",
            },
        )
        self.assertEqual(401, response.status_code)
        self.assertEqual("User login failed.", response.data["detail"])
