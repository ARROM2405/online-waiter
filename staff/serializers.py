from rest_framework import serializers

from staff.models import Staff, Waiter


class StaffBaseSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = (
            "id",
            "currently_employed",
            "username",
        )

    def get_username(self, obj):
        return obj.user.username


class WaiterSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Waiter


class UserLogInRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserLogInResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    token = serializers.CharField()
