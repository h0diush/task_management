from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import CRUMixin
from groups.models import Group
from groups.permissions import IsOwnerPermission
from groups.serializers.api.groups import GroupCreateSerializer, \
    GroupRetrieveSerializer


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
    serializer_class = GroupCreateSerializer
    permission_classes = [IsOwnerPermission]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == "create":
            return GroupCreateSerializer
        if self.action == "retrieve":
            return GroupRetrieveSerializer
