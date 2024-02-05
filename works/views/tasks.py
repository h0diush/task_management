from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import LCRUDMixin
from works.models import Task
from works.permissions import CreateTaskPermission
from works.serializers.api.tasks import TaskCreateSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Добавить задачу",
        tags=["Задачи"]
    ),
    # retrieve=extend_schema(
    #     summary="Посмотреть сотрудника",
    #     tags=["Сотрудники"]
    # ),
    # partial_update=extend_schema(summary="Изменить сотрудника частично",
    #                              tags=["Задачи"]),
    # list=extend_schema(
    #     summary="Список сотрудников",
    #     tags=["Задачи"]
    # ),
    # destroy=extend_schema(
    #     summary="Удалить сотрудника",
    #     tags=["Задачи"]
    # ),
)
class TaskView(LCRUDMixin):
    queryset = Task.objects.all()
    multi_serializer_class = {
        'create': TaskCreateSerializer
    }
    http_method_names = ['post']
    lookup_url_kwarg = 'task_id'
    permission_classes = [CreateTaskPermission]
