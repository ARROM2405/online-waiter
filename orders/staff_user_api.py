from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import OrderDestroyPermission, OrderUpdatePermission
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == "destroy":
            permission_classes.append(OrderDestroyPermission)
        elif self.action == "update":
            permission_classes.append(OrderUpdatePermission)
        return [permission() for permission in permission_classes]
