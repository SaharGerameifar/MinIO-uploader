from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    The request is owner as a user.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and obj.user == request.user
        )


  