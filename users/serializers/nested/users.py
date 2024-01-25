from common.serializers.mixins import ExtendedModelSerializerMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserShortSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name')
