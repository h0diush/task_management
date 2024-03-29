from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializerMixin

User = get_user_model()


class RegisterSerializer(ExtendedModelSerializerMixin):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_style': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )

    @staticmethod
    def _validate_username_or_email(value):
        username_or_email = value.lower()
        if User.objects.filter(email=username_or_email).exists():
            raise ParseError(
                f"Пользователь c {username_or_email} уже существует")
        return username_or_email

    def validated_username(self, value):
        return self._validate_username_or_email(value)

    def validate_email(self, value):
        return self._validate_username_or_email(value)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(ExtendedModelSerializerMixin):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError("Проверьте правильность ввода текущего пароля")
        return attrs

    def validate_new_password(self, value):
        return validate_password(value)

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'phone_number',
            'date_joined'
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'phone_number',
        )