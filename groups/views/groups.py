from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import CRUMixin
from groups.models import Group
from groups.permissions import IsAdministratorOrEmployeesPermission
from groups.serializers.api.groups import GroupCreateSerializer, \
    GroupRetrieveSerializer, GroupUpdateSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Добавить группу",
        tags=["Группы"]
    ),
    retrieve=extend_schema(
        summary="Посмотреть группу",
        tags=["Группы"]
    ),
    partial_update=extend_schema(summary="Изменить группу частично",
                                 tags=["Группы"]),
)
class GroupsView(CRUMixin):
    queryset = Group.objects.all()
    permission_classes = [IsAdministratorOrEmployeesPermission]
    http_method_names = ['get', 'post', 'patch']

    multi_serializer_class = {
        'create': GroupCreateSerializer,
        'retrieve': GroupRetrieveSerializer,
        'partial_update': GroupUpdateSerializer
    }
