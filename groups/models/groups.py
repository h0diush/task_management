from django.conf import settings
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=155, verbose_name="Название группы")
    administrator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      verbose_name="Администратор",
                                      related_name='groups_administrator')
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     verbose_name="Работники группы",
                                     related_name='groups_workers')
    jobs = models.ForeignKey('works.Job', on_delete=models.CASCADE,
                             verbose_name="Работа", related_name='groups',
                             null=True, blank=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ('name',)

    def __str__(self):
        return self.name
