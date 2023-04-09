from django.contrib.auth.models import User


def if_user_is_manager(user: User) -> bool:
    return hasattr(user, "manager")


def if_user_is_waiter(user: User) -> bool:
    return hasattr(user, "waiter")
