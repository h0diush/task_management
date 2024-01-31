from django.db import models
from common.models.mixins import InfoMixin


class Job(InfoMixin):
    deadline = models.DateTimeField(verbose_name='Срок выполнения')
    task = models.ManyToManyField('works.Task', verbose_name='Задача',
                                  related_name='job_tasks', blank=True,
                                  )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name
