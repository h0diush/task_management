from rest_framework.permissions import BasePermission


class IsCreatedByWork(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.created_by == request.user:
            return True
        return False
