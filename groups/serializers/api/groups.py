from crum import get_current_user

from common.serializers.mixins import ExtendedModelSerializerMixin
from groups.models import Group
from users.serializers.nested.users import UserShortSerializer


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

    class Meta:
        model = Group
        fields = ('name', 'administrator', 'jobs', 'employees')


