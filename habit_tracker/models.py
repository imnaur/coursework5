from datetime import timedelta

from django.conf import settings
from django.db import models


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Создатель привычки",
        max_length=50,
        on_delete=models.CASCADE,
    )
    location = models.CharField(
        verbose_name="Место выполнения привычки", max_length=255
    )
    time = models.TimeField(verbose_name="Время выполнения привычки")
    action = models.TextField(verbose_name="Действие привычки")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        null=True,
        blank=True,
    )
    compensation = models.CharField(
        max_length=255, verbose_name="Вознаграждение", null=True, blank=True
    )
    regularity = models.IntegerField(default=1, verbose_name="Периодичность в днях")
    time_required = models.DurationField(
        verbose_name="Время на выполнение", default=timedelta(minutes=2)
    )
    public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
