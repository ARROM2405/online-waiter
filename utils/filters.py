from django_filters.constants import EMPTY_VALUES
from django_filters.rest_framework.filters import CharFilter
from rest_framework.exceptions import ValidationError


class CommaSeparatedIntFilter(CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        try:
            value = [int(value_unit) for value_unit in value.split(",")]
        except TypeError:
            raise ValidationError(
                f"Invalid value passed to {self.field_name}. Has to be int separated by comma. Example: 1,2,33,4"
            )
        lookup = f"{self.field_name}"
        qs = self.get_method(qs)(**{lookup: value})
        if self.distinct:
            qs.distinct()
        return qs


def get_look_up_expression_from_the_filter_name(filter_name):
    if len(split_filter_name := filter_name.split("__")) == 2:
        return split_filter_name[1]
    return "exact"
