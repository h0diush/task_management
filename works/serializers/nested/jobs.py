from common.serializers.mixins import ExtendedModelSerializerMixin
from works.models import Job
from works.serializers.nested.tasks import TaskShortSerializer


class JobShortSerializer(ExtendedModelSerializerMixin):
    task = TaskShortSerializer(many=True)

    class Meta:
        model = Job
        fields = (
            'id', 'deadline', 'name', 'description', 'created_by',
            'updated_by', 'task')
