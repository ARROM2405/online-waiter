from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import OrderUpdatePermission
from orders.models import Order
from orders.serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = (
        Order.objects.select_related("tip", "waiter")
        .prefetch_related("food_set", "beverage_set")
        .all()
        .order_by("-id")
    )

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == "update":
            permission_classes.append(OrderUpdatePermission)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        if self.action == "retrieve":
            return OrderDetailSerializer
        elif self.action == "update":
            return OrderUpdateSerializer
