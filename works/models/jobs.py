from django.db import models
from common.models.mixins import InfoMixin


class Job(InfoMixin):
    deadline = models.DateTimeField(verbose_name='Срок выполнения')
    task = models.ManyToManyField('works.Task', verbose_name='Задача',
                                  related_name='job_tasks', blank=True,
                                  )
    active = models.BooleanField(default=True, verbose_name='Активная')
    group = models.ForeignKey('groups.Group', verbose_name='Группа',
                              on_delete=models.CASCADE, blank=True, null=True,
                              related_name='jobs_group')

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name
