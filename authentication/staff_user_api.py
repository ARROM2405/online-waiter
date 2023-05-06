from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from authentication.exceptions import LoginFailedException
from staff.serializers import UserLogInRequestSerializer, UserLogInResponseSerializer
from authentication.staff_user_services import UserLogInService


class UserLoginViewSet(viewsets.GenericViewSet):
    serializer_class = UserLogInRequestSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request):
        request_serializer = self.serializer_class(data=request.data)
        if request_serializer.is_valid():
            response_data = UserLogInService(
                **request_serializer.validated_data
            ).get_staff_user_with_token()
            response_serializer = UserLogInResponseSerializer(data=response_data)
            response_serializer.is_valid()
            return Response(
                data=response_serializer.validated_data,
                status=HTTP_200_OK,
            )
        else:
            raise LoginFailedException
