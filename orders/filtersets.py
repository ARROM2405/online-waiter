from django_filters.rest_framework import FilterSet, filters

from orders.models import Order


class OrderFilterSet(FilterSet):
    is_tipped = filters.BooleanFilter(field_name="tip", method="filter_tipped")

    def filter_tipped(self, queryset, name, value):
        return queryset.exclude(tip__isnul=value)

    # TODO: add filter by total sum of the F&B

    class Meta:
        model = Order
        fields = {
            "id": ["exact"],
            "payment_status": ["exact"],
            "table": ["exact", "in"],
            "waiter__username": ["exact"],
            "ordering_type": ["exact"],
            "submit_timestamp": ["exact", "gt", "gte", "lt", "lte"],
            "last_update_timestamp": ["exact", "gt", "gte", "lt", "lte"],
        }
