from rest_framework import serializers


class StaffBaseSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        fields = ("currently_employed",)

    def get_username(self):
        return self.user.username


class WaiterSerializer(StaffBaseSerializer):
    pass
