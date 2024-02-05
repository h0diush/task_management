from rest_framework.permissions import BasePermission
import bdb


class IsCreatedByWork(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.created_by == request.user:
            return True
        return False


class CreateTaskPermission(BasePermission):
    def has_permission(self, request, view):
        job_id = view.kwargs['pk']
        user = request.user
        if user.groups_administrator.filter(jobs__id=job_id).exists():
            return True
        return False

