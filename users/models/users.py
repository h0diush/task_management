from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=75, verbose_name="Имя пользователя",
                                unique=True)
    email = models.EmailField("Электронная почта", unique=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", unique=True,
                                    null=True)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.full_name} ({self.pk})"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
