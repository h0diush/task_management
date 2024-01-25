from django.db import models
from common.models.mixins import InfoMixin


class Job(InfoMixin):
    deadline = models.DateTimeField(verbose_name='Срок выполнения')
    task = models.ForeignKey('works.Task', verbose_name='Задача',
                             on_delete=models.SET_NULL, related_name='jobs',
                             blank=True, null=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name

