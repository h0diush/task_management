from crum import get_current_user
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializerMixin
from works.models import Task, Job


class TaskCreateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Task
        fields = ('doer', 'name', 'description')

    def _get_job(self):
        job_id = self.context['view'].kwargs.get('pk')
        user = get_current_user()
        job = Job.objects.filter(pk=job_id, created_by=user).first()
        return job

    def create(self, validated_data):
        job = self._get_job()
        if not job:
            raise ParseError(detail="Такой работы не существует")
        validated_data['job'] = job
        instance = super(TaskCreateSerializer, self).create(validated_data)
        job.task.add(instance)
        return instance
