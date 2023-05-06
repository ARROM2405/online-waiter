from rest_framework import serializers

from staff.models import Staff


class StaffBaseSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ("currently_employed",)

    def get_username(self):
        return self.user.username


class WaiterSerializer(StaffBaseSerializer):
    pass


class UserLogInRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserLogInResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    token = serializers.CharField()
