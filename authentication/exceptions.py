from rest_framework.exceptions import APIException, status


class LoginFailedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "User login failed."
