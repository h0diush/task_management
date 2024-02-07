from django.db.models import Count
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
    permission_classes = [IsAdministratorOrEmployeesPermission]
    http_method_names = ['get', 'post', 'patch']

    multi_serializer_class = {
        'create': GroupCreateSerializer,
        'retrieve': GroupRetrieveSerializer,
        'partial_update': GroupUpdateSerializer
    }

    def get_queryset(self):
        qs = Group.objects.all().select_related(
            'administrator'
        ).prefetch_related(
            'employees', 'jobs'
        ).annotate(
            count_employees=Count('employees', distinct=True),
            count_jobs=Count('jobs', distinct=True)
        )
        return qs
