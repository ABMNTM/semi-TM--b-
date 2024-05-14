from rest_framework.permissions import IsAuthenticated , BasePermission
from django.contrib.auth.models import User


class IsAuthenticatedAndOwner(BasePermission):

    message = 'permission denied, you are not the object owner.'

    has_permission = IsAuthenticated.has_permission
    
    def has_object_permission(self, request, view, obj):

        return bool(request.user == obj)