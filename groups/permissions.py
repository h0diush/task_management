from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdministratorOrEmployeesPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.administrator == request.user:
            return True
        if request.method in SAFE_METHODS:
            return request.user in obj.employees.all()
        return False


class IsAdministrator(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.group.administrator == request.user:
            return True
        return False
