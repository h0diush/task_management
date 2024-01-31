from common.serializers.mixins import ExtendedModelSerializerMixin
from works.models import Task


class TaskShortSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Task
        fields = ('id', 'doer', 'status', 'name', 'description', 'created_by')
