from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Адрес почты')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    chat_id = models.IntegerField(verbose_name='ID телеграм', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
