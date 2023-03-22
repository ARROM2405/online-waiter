from rest_framework import serializers

from orders.models import Order, Table
from staff.serializers import WaiterSerializer


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("number",)


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(required=True)
    waiter = WaiterSerializer()

    class Meta:
        model = Order
        fields = ("table",)
