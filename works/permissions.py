from rest_framework.permissions import BasePermission, SAFE_METHODS


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
        if request.method in SAFE_METHODS:
            return user.groups_employee.filter(
                jobs__id=job_id).exists()
        return False


class UpdateStatusTaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.created_by == request.user or obj.doer == request.user:
            return True
        return False
