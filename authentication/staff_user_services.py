import typing
from contextlib import suppress

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token


from authentication.exceptions import LoginFailedException
from staff.models import Manager, Waiter, Staff


class UserLogInService:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_staff_user_with_token(self) -> dict:
        staff_user = self._get_staff_user()
        token, _ = Token.objects.get_or_create(user=staff_user.user)
        return {"user_id": staff_user.id, "token": token.key}

    def _get_staff_user(self) -> typing.Optional[Staff]:
        manager_user = None
        waiter_user = None
        with suppress(ObjectDoesNotExist):
            manager_user = Manager.objects.get(
                user__username=self.username,
                user__password=self.password,
            )
            waiter_user = Waiter.objects.get(
                user__username=self.username,
                user__password=self.password,
            )
        if any((manager_user, waiter_user)):
            return manager_user or waiter_user
        raise LoginFailedException
