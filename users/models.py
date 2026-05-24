from django.db import models


class CustomUser(models.Model):
    user = models.CharField(max_length=50, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
