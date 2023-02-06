from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # SAFE_METHOD = ['GET', 'PUT', 'POST', 'PATCH']
        if request.method in SAFE_METHODS:
            return bool(True)
        return bool(request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = ['GET', 'PUT', 'POST', 'PATCH']
        if request.method in SAFE_METHODS:
            return bool(True)
        return bool(request.user and request.user.is_authenticated and (request.user.role == "ADMIN" or request.user == obj.created_by))
    


