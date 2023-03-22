from rest_framework import serializers

from orders.models import Order

class TableSerializer(serializers.ModelSerializer):


# TODO: add nested serializer for display ??
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("table",)
