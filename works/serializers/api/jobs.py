from crum import get_current_user
from django.db import transaction
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializerMixin
from groups.models import Group
from works.models import Job
from works.serializers.nested.tasks import TaskShortSerializer


class JobRetrieveSerializer(ExtendedModelSerializerMixin):
    task = TaskShortSerializer(many=True)

    class Meta:
        model = Job
        fields = ('id', 'name', 'description', 'created_by', 'task')


class JobCreateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Job
        fields = ('id', 'name', 'description', 'deadline')

    def _get_group(self):
        user = get_current_user()
        group = Group.objects.filter(administrator=user).first()
        if not group:
            raise ParseError(detail='У вас недостаточно прав')
        return group

    def create(self, validated_data):
        group = self._get_group()
        validated_data['group'] = group
        instance = super(JobCreateSerializer, self).create(validated_data)
        with transaction.atomic():
            group.jobs.add(instance)
        return instance


class JobUpdateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Job
        fields = ('id', 'name', 'description')


class JobDeleteSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Job
        fields = ('id',)


class JobListSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Job
        fields = ('id', 'name', 'description', 'deadline', 'created_by')
