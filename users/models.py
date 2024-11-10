from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name='Страна')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар')
    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='Токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email