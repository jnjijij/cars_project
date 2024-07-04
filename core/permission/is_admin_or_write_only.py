from rest_framework.permissions import BasePermission

from core.dataclass.user_dataclass import UserDataClass


class IsAdminOrWriteOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        user: UserDataClass = request.user
        return user.is_staff
