from config import settings
from django.db import models
from django.utils import timezone


class DateMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано когда', null=True, blank=False
    )
    updated_at = models.DateTimeField(
        verbose_name='Изменено когда', null=True, blank=False
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)


class InfoMixin(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True,
                                   blank=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='created_%(app_label)s_%(class)s',
        verbose_name="Сделано", null=True
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='updated%(app_label)s_%(class)s',
        verbose_name="Изменено", null=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(InfoMixin, self).save(*args, **kwargs)
