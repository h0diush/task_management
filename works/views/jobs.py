from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated

from common.views.mixins import LCRUDMixin
from works.models import Job
from works.serializers.api.jobs import JobRetrieveSerializer, \
    JobCreateSerializer, JobUpdateSerializer, JobListSerializer, \
    JobDeleteSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Создать работу",
        tags=["Работа"]
    ),
    retrieve=extend_schema(
        summary="Посмотреть работу",
        tags=["Работа"]
    ),
    partial_update=extend_schema(summary="Изменить работу частично",
                                 tags=["Работа"]),
    destroy=extend_schema(
        summary="Удалить работу",
        tags=["Работа"]
    ),
    list=extend_schema(
        summary="Список Задач",
        tags=["Работа"]
    ),
)
class JobViewSet(LCRUDMixin):
    multi_serializer_class = {
        'create': JobCreateSerializer,
        'retrieve': JobRetrieveSerializer,
        'partial_update': JobUpdateSerializer,
        'list': JobListSerializer,
        'destroy': JobDeleteSerializer
    }
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    lookup_url_kwarg = 'job_id'

    def get_queryset(self):
        return Job.objects.filter(created_by=self.request.user)
