from rest_framework import serializers

from food_and_beverage.models import Food, FoodAndBeverageBase, Beverage


class FoodAndBeverageSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = FoodAndBeverageBase
        fields = (
            "name",
            "description",
            "price",
            "order",
            "units_available",
        )


class FoodSerializer(FoodAndBeverageSerializerBase):
    class Meta:
        model = Food
        fields = FoodAndBeverageSerializerBase.Meta.fields + ("type",)


class BeverageSerializer(FoodAndBeverageSerializerBase):
    class Meta:
        model = Beverage
        fields = FoodAndBeverageSerializerBase.Meta.fields + (
            "Type",
            "alcoholic",
        )
