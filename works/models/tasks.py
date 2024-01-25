from django.db import models

from common.models.mixins import InfoMixin


class StatusChoice(models.TextChoices):
    DONE = "Done", "Выполнено"
    IN_PROGRESS = "In progress", "В процессе разработки"
    FAMILIARIZATION = "Familiarization", "Ознакомление с задачами"
    NOT_COMPLETED = "Not completed", "Не выполнено"
    REVIEW_OF_THE_DOER = "Review of the doer", "На рассмотрении у исполнителя"


class Task(InfoMixin):
    doer = models.ForeignKey('users.User', verbose_name='Исполнитель',
                             on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=StatusChoice,
                              verbose_name="Статус",
                              default=StatusChoice.REVIEW_OF_THE_DOER)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name
