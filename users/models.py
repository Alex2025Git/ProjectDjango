from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email address')

    token = models.CharField(max_length=110, verbose_name='Токен', blank=True, unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='phone number', blank=True, null=True, help_text='Введите номер телефона')
    nik_name = models.CharField(max_length=50, unique=True, verbose_name='Ваш Ник', blank=True, null=True, help_text='Укажите Ник')
    avatar = models.ImageField(upload_to='avatar', verbose_name='Аватар', blank=True, null=True, help_text='Загрузите свой аватар')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email