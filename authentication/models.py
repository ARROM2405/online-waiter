from rest_framework.permissions import BasePermission

from utils.check_user import if_user_is_manager, if_user_is_waiter


class OrderDestroyPermission(BasePermission):
    def has_permission(self, request, view):
        return if_user_is_manager(request.user)


class OrderUpdatePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if if_user_is_manager(request.user):
            return True
        elif if_user_is_waiter(request.user):
            if obj.waiter == request.user.waiter:
                return True
        return False
