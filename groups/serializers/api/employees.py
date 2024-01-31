from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializerMixin
from groups.models import Employee, Group
from users.serializers.nested.users import UserShortSerializer

User = get_user_model()


class EmployeeListSerializer(ExtendedModelSerializerMixin):
    user = UserShortSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'date_joined')


class EmployeeDestroySerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Employee
        fields = ('id',)


class EmployeeCreateSerializer(EmployeeDestroySerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def validate(self, attrs):
        current_user = get_current_user()
        group_id = self.context['view'].kwargs.get('pk')
        group = Group.objects.filter(pk=group_id,
                                     administrator=current_user).first()
        if not group:
            raise ParseError("Такой группы не найдено")
        attrs['group'] = group
        return attrs

    def create(self, validated_data):
        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password')
        }
        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            validated_data['user'] = user
            instance = super().create(validated_data)
        return instance


class EmployeeUpdateSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeRetrieveSerializer(ExtendedModelSerializerMixin):
    class Meta:
        model = Employee
        fields = '__all__'
