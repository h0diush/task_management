from crum import get_current_user
from rest_framework import serializers

from common.serializers.mixins import ExtendedModelSerializerMixin
from groups.models import Group
from users.serializers.nested.users import UserShortSerializer
from works.serializers.nested.jobs import JobShortSerializer


class GroupCreateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Group
        fields = ('name',)

    def create(self, validated_data):
        administrator = get_current_user()
        validated_data['administrator'] = administrator
        instance = super(GroupCreateSerializer, self).create(validated_data)
        return instance


class GroupRetrieveSerializer(ExtendedModelSerializerMixin):
    administrator = UserShortSerializer()
    employees = UserShortSerializer(many=True)
    jobs = JobShortSerializer(many=True)
    count_employees = serializers.IntegerField()
    count_jobs = serializers.IntegerField()

    class Meta:
        model = Group
        fields = (
            'name', 'administrator', 'employees', 'jobs', 'count_employees',
            'count_jobs'
        )


class GroupUpdateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Group
        fields = ('id', 'name', 'jobs')
