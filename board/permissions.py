from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAuthenticatedAndOwner(BasePermission):

    has_permission = IsAuthenticated.has_permission

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.owner)