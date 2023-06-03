from _decimal import Decimal
from enumfields.drf import EnumField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from food_and_beverage.models import Food, Beverage
from food_and_beverage.serializers import (
    SlimFoodSerializer,
    SlimBeverageSerializer,
)
from orders.enums import OrderPaymentStatus, OrderPreparationSatus, OrderingType
from orders.models import Order, Table
from staff.models import Waiter
from staff.serializers import WaiterSerializer
from utils.utils import (
    ManyToManyListField,
)


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = (
            "id",
            "number",
            "status",
        )


class OrderBaseSerializer(serializers.ModelSerializer):
    table = TableSerializer(required=True)
    waiter = WaiterSerializer()
    food_set = SlimFoodSerializer(many=True)
    beverage_set = SlimBeverageSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "table",
            "waiter",
            "food_set",
            "beverage_set",
        )

    def validate(self, attrs):
        super().validate(attrs)
        if attrs.get("food_set") is None and attrs.get("beverage_set") is None:
            raise ValidationError("Order has to include at least one food or beverage.")
        return attrs


class OrderListSerializer(OrderBaseSerializer):
    pass


class OrderDetailSerializer(OrderBaseSerializer):
    tip = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = OrderBaseSerializer.Meta.fields + (
            "payment_status",
            "preparation_status",
            "ordering_type",
            "tip",
            "comment",
        )

    def get_tip(self, obj):
        if hasattr(obj, "tip"):
            return obj.tip.amount
        return Decimal("0.00")


class OrderUpdateSerializer(serializers.Serializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(),
        write_only=True,
        source="table",
    )
    waiter = WaiterSerializer(read_only=True)
    waiter_id = serializers.PrimaryKeyRelatedField(
        queryset=Waiter.objects.all(),
        write_only=True,
        source="waiter",
    )
    food_set = SlimFoodSerializer(
        many=True,
        read_only=True,
    )
    food_set_ids = ManyToManyListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Food.objects.all()),
        write_only=True,
        source="food_set",
    )
    beverage_set = SlimBeverageSerializer(
        many=True,
        read_only=True,
    )
    beverage_set_ids = ManyToManyListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Beverage.objects.all()),
        write_only=True,
        source="beverage_set",
    )
    payment_status = EnumField(OrderPaymentStatus)
    preparation_status = EnumField(OrderPreparationSatus)
    ordering_type = EnumField(OrderingType)

    def update(self, instance, validated_data):
        instance.table = validated_data["table"]
        instance.waiter = validated_data["waiter"]
        instance.payment_status = validated_data["payment_status"]
        instance.preparation_status = validated_data["preparation_status"]
        instance.ordering_type = validated_data["ordering_type"]
        for food in validated_data["food_set"]:
            instance.food_set.add(food)
        for beverage in validated_data["beverage_set"]:
            instance.beverage_set.add(beverage)
        instance.save()
        return instance
