from django.contrib.auth.models import BaseUserManager
from rest_framework.exceptions import ParseError


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number=None, email=None, password=None,
                     username=None, **extra_fields):
        if not (phone_number or not email or username):
            raise ParseError(
                "Укажите email, имя пользователя и номер телефона"
            )
        if email:
            email = self.normalize_email(email)

        if not username:
            if email:
                username = email
            else:
                username = phone_number
        user = self.model(username=username, **extra_fields)

        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, email=None, username=None,
                    password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(phone_number, email, username, password,
                                 **extra_fields)

    def create_superuser(self, phone_number=None, email=None, username=None,
                         password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self._create_user(phone_number, email, username, password,
                                 **extra_fields)
