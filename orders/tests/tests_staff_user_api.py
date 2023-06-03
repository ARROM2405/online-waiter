from _decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse

from food_and_beverage.tests.factories import FoodFactory, BeverageFactory
from orders.enums import OrderPreparationSatus
from orders.models import Order
from orders.tests.factories import OrderFactory
from utils.tests.test_base import StaffApiTestBase


class TestOrderViewSet(StaffApiTestBase):
    def setUp(self):
        super().setUp()
        self.order_1 = OrderFactory()
        self.order_2 = OrderFactory()
        self.food_1 = FoodFactory()
        self.food_2 = FoodFactory()
        self.beverage_1 = BeverageFactory()
        self.beverage_2 = BeverageFactory()
        self.order_1.food_set.add(self.food_1)
        self.order_1.beverage_set.add(self.beverage_1)
        self.order_1.save()
        self.order_2.food_set.add(self.food_2)
        self.order_2.beverage_set.add(self.beverage_2)
        self.order_2.save()
        self.other_waiter = self.order_1.waiter

    def _get_order_request_data(self, order: Order) -> dict:
        food_set = [food.id for food in order.food_set.all()]

        beverage_set = [beverage.id for beverage in order.beverage_set.all()]
        data = {
            "table_id": order.table.id,
            "waiter_id": order.waiter.id,
            "food_set_ids": food_set,
            "beverage_set_ids": beverage_set,
            "payment_status": order.payment_status,
            "preparation_status": order.preparation_status,
            "ordering_type": order.ordering_type,
        }
        return data

    def test_list_orders_ok(self):
        token = self._generate_token_for_existing_user(staff_user=self.manager_user)
        response = self.client.get(
            path=reverse("order-list"),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = response.data
        self.assertEqual(2, len(data))
        order_response_data = data[0]
        self.assertEqual(order_response_data["id"], self.order_2.id)
        self.assertEqual(
            order_response_data["table"]["number"],
            self.order_2.table.number,
        )
        self.assertEqual(
            order_response_data["waiter"]["username"],
            self.order_2.waiter.user.username,
        )
        self.assertEqual(
            order_response_data["food_set"][0]["name"],
            self.food_2.name,
        )
        self.assertEqual(
            order_response_data["beverage_set"][0]["name"],
            self.beverage_2.name,
        )

    def test_list_orders_invalid_token(self):
        response = self.client.get(
            path=reverse("order-list"),
            HTTP_AUTHORIZATION=f"Token incorrect_token",
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail_order_ok(self):
        token = self._generate_token_for_existing_user(staff_user=self.manager_user)
        response = self.client.get(
            path=reverse("order-detail", kwargs={"pk": self.order_1.id}),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = response.data
        self.assertEqual(self.order_1.id, data["id"])
        self.assertEqual(
            self.order_1.waiter.user.username,
            data["waiter"]["username"],
        )
        self.assertEqual(self.food_1.name, data["food_set"][0]["name"])
        self.assertEqual(
            self.beverage_1.name,
            data["beverage_set"][0]["name"],
        )
        self.assertEqual(self.order_1.payment_status, data["payment_status"])
        self.assertEqual(
            self.order_1.preparation_status,
            data["preparation_status"],
        )
        self.assertEqual(self.order_1.ordering_type, data["ordering_type"])
        self.assertEqual(Decimal("0.00"), data["tip"])

    def test_detail_order_not_found(self):
        token = self._generate_token_for_existing_user(staff_user=self.manager_user)
        response = self.client.get(
            path=reverse("order-detail", kwargs={"pk": self.order_2.id + 100}),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_detail_invalid_token_provided(self):
        response = self.client.get(
            path=reverse("order-detail", kwargs={"pk": self.order_2.id + 100}),
            HTTP_AUTHORIZATION=f"Token invalid_token",
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update_order_ok(self):
        token = self._generate_token_for_existing_user(staff_user=self.order_1.waiter)
        self.assertEqual(OrderPreparationSatus.NEW, self.order_1.preparation_status)
        data = self._get_order_request_data(self.order_1)
        data["preparation_status"] = OrderPreparationSatus.PREPARING
        response = self.client.put(
            path=reverse("order-detail", kwargs={"pk": self.order_1.id}),
            data=data,
            HTTP_AUTHORIZATION=f"Token {token.key}",
            content_type="application/json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.order_1.refresh_from_db()
        self.assertEqual(
            OrderPreparationSatus.PREPARING,
            self.order_1.preparation_status,
        )

    def test_update_order_by_manager(self):
        token = self._generate_token_for_existing_user(staff_user=self.manager_user)
        self.assertEqual(OrderPreparationSatus.NEW, self.order_1.preparation_status)
        data = self._get_order_request_data(self.order_1)
        data["preparation_status"] = OrderPreparationSatus.PREPARING
        response = self.client.put(
            path=reverse("order-detail", kwargs={"pk": self.order_1.id}),
            data=data,
            HTTP_AUTHORIZATION=f"Token {token.key}",
            content_type="application/json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_order_no_permission(self):
        token = self._generate_token_for_existing_user(staff_user=self.waiter_user)
        data = self._get_order_request_data(self.order_1)
        response = self.client.put(
            path=reverse("order-detail", kwargs={"pk": self.order_1.id}),
            data=data,
            HTTP_AUTHORIZATION=f"Token {token.key}",
            content_type="application/json",
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_update_order_not_all_data_provided(self):
        token = self._generate_token_for_existing_user(staff_user=self.order_1.waiter)
        data = self._get_order_request_data(self.order_1)
        data.pop("table_id")
        response = self.client.put(
            path=reverse("order-detail", kwargs={"pk": self.order_1.id}),
            data=data,
            HTTP_AUTHORIZATION=f"Token {token.key}",
            content_type="application/json",
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
