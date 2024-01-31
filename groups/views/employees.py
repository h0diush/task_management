from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import LCRUDMixin
from groups.models import Employee
from groups.permissions import IsAdministrator
from groups.serializers.api.employees import EmployeeCreateSerializer, \
    EmployeeRetrieveSerializer, EmployeeDestroySerializer, \
    EmployeeListSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Добавить сотрудника",
        tags=["Сотрудники"]
    ),
    retrieve=extend_schema(
        summary="Посмотреть сотрудника",
        tags=["Сотрудники"]
    ),
    partial_update=extend_schema(summary="Изменить сотрудника частично",
                                 tags=["Сотрудники"]),
    list=extend_schema(
        summary="Список сотрудников",
        tags=["Сотрудники"]
    ),
    destroy=extend_schema(
        summary="Удалить сотрудника",
        tags=["Сотрудники"]
    ),
)
class EmployeesView(LCRUDMixin):
    queryset = Employee.objects.all()
    multi_serializer_class = {
        'create': EmployeeCreateSerializer,
        'retrieve': EmployeeRetrieveSerializer,
        'update': EmployeeRetrieveSerializer,
        'destroy': EmployeeDestroySerializer,
        'list': EmployeeListSerializer
    }
    permission_classes = [IsAdministrator]
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_url_kwarg = 'employee_id'
