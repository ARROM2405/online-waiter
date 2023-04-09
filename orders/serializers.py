from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from food_and_beverage.serializers import FoodSerializer, BeverageSerializer
from orders.models import Order, Table
from staff.serializers import WaiterSerializer


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("number",)


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(required=True)
    waiter = WaiterSerializer()
    food = FoodSerializer(many=True)
    beverage = BeverageSerializer(many=True)

    class Meta:
        model = Order
        fields = ("table",)

    def validate(self, attrs):
        super().validate(attrs)
        if self.food is None and self.beverage is None:
            raise ValidationError("Order has to include at least one food or beverage.")
