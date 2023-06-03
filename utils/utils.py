from enum import IntEnum

from rest_framework import serializers


class EnhancedIntEnum(IntEnum):
    @classmethod
    def list_values(cls):
        return [member.value for member in cls]


class ManyToManyListField(serializers.ListField):
    def to_representation(self, data):
        return [obj.id for obj in data.all()]
