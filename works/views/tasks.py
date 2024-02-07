from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from common.views.mixins import LCRUDMixin
from works.models import Task
from works.permissions import CreateTaskPermission, UpdateStatusTaskPermission
from works.serializers.api.tasks import TaskCreateSerializer, \
    TaskListSerializer, TaskDetailSerializer, TaskDestroySerializer, \
    TaskUpdateStatusSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Добавить задачу",
        tags=["Задачи"]
    ),
    retrieve=extend_schema(
        summary="Посмотреть задачу",
        tags=["Задачи"]
    ),
    partial_update=extend_schema(summary="Изменить задачу частично",
                                 tags=["Задачи"]),
    list=extend_schema(
        summary="Список задач",
        tags=["Задачи"]
    ),
    destroy=extend_schema(
        summary="Удалить задачу",
        tags=["Задачи"]
    ),
    update_status_task=extend_schema(summary="Изменить статус задачи",
                                     tags=["Задачи"]),
)
class TaskView(LCRUDMixin):
    queryset = Task.objects.all()
    multi_serializer_class = {
        'create': TaskCreateSerializer,
        'list': TaskListSerializer,
        'retrieve': TaskDetailSerializer,
        'destroy': TaskDestroySerializer,
        'partial_update': TaskCreateSerializer,
        'update_status_task': TaskUpdateStatusSerializer
    }
    http_method_names = ['post', 'get', 'delete', 'patch']
    lookup_url_kwarg = 'task_id'
    permission_classes = [CreateTaskPermission]

    def get_queryset(self):
        qs = Task.objects.filter(job__id=self.kwargs['pk']).select_related(
            'doer', 'job')
        return qs

    @action(detail=True, methods=['post'],
            permission_classes=[UpdateStatusTaskPermission])
    def update_status_task(self, request, *args, **kwargs):
        serializer = self.multi_serializer_class['update_status_task'](
            instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            TaskListSerializer(instance=serializer.instance).data)
