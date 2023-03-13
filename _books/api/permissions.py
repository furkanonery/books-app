from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )
    
class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
    
class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
    

class IsCommenterOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in SAFE_METHODS or
            obj.commenter == request.user
        )

