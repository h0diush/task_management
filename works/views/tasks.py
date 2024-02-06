from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import LCRUDMixin
from works.models import Task
from works.permissions import CreateTaskPermission
from works.serializers.api.tasks import TaskCreateSerializer, \
    TaskListSerializer, TaskDetailSerializer, TaskDestroySerializer


@extend_schema_view(
    create=extend_schema(
        summary="Добавить задачу",
        tags=["Задачи"]
    ),
    retrieve=extend_schema(
        summary="Посмотреть задачу",
        tags=["Задачи"]
    ),
    # partial_update=extend_schema(summary="Изменить сотрудника частично",
    #                              tags=["Задачи"]),
    list=extend_schema(
        summary="Список задач",
        tags=["Задачи"]
    ),
    destroy=extend_schema(
        summary="Удалить задачу",
        tags=["Задачи"]
    ),
)
class TaskView(LCRUDMixin):
    queryset = Task.objects.all()
    multi_serializer_class = {
        'create': TaskCreateSerializer,
        'list': TaskListSerializer,
        'retrieve': TaskDetailSerializer,
        'destroy': TaskDestroySerializer,
    }
    http_method_names = ['post', 'get', 'delete']
    lookup_url_kwarg = 'task_id'
    permission_classes = [CreateTaskPermission]

    def get_queryset(self):
        qs = Task.objects.filter(job__id=self.kwargs['pk'])
        return qs
