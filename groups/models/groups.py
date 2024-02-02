from django.conf import settings
from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=155, verbose_name="Название группы")
    administrator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.RESTRICT,
                                      verbose_name="Администратор",
                                      related_name='groups_administrator')
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       verbose_name="Работники группы",
                                       related_name='groups_employee',
                                       blank=True, through='Employee')
    jobs = models.ManyToManyField('works.Job', verbose_name="Работа",
                                  related_name='group_jobs', blank=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Employee(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              related_name='employees_info',
                              verbose_name="Группа")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='groups_info',
                             verbose_name="Пользователь")
    date_joined = models.DateTimeField(default=timezone.now,
                                       verbose_name="Добавлен")

    class Meta:
        verbose_name = 'Сотрудник группы'
        verbose_name_plural = 'Сотрудники групп'
        ordering = ('-date_joined',)
        unique_together = (('group', 'user'),)

    def __str__(self):
        return f'Сотрудник {self.user}'
