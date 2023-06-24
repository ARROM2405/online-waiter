from django.db.models import F
from django_filters.rest_framework import FilterSet, filters

from orders.models import Order
from utils.filters import (
    CommaSeparatedIntFilter,
    get_look_up_expression_from_the_filter_name,
)


class OrderFilterSet(FilterSet):
    is_tipped = filters.BooleanFilter(field_name="tip", method="filter_tipped")

    items_total_price = filters.NumberFilter(method="filter_items_total_price")
    items_total_price__lt = filters.NumberFilter(method="filter_items_total_price")
    items_total_price__lte = filters.NumberFilter(method="filter_items_total_price")
    items_total_price__gt = filters.NumberFilter(method="filter_items_total_price")
    items_total_price__gte = filters.NumberFilter(method="filter_items_total_price")

    table__in = CommaSeparatedIntFilter()

    def filter_tipped(self, queryset, name, value):
        return queryset.exclude(tip__isnull=value)

    def filter_items_total_price(self, queryset, name, value):
        lookup_expr = get_look_up_expression_from_the_filter_name(name)
        look_up_field = "total_items_price"
        filtered_queryset = queryset.annotate(
            total_items_price=F("total_food_price") + F("total_beverage_price")
        ).filter(**{look_up_field + "__" + lookup_expr: value})
        return filtered_queryset

    class Meta:
        model = Order
        fields = {
            "id": ["exact"],
            "payment_status": ["exact"],
            "table": ["exact"],
            "waiter": ["exact"],
            "ordering_type": ["exact"],
            "submit_timestamp": ["exact", "gt", "gte", "lt", "lte"],
            "last_update_timestamp": ["exact", "gt", "gte", "lt", "lte"],
        }
