from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    # name = models.CharField('Имя', max_length=32, blank=False)
    # nick = models.CharField('Ник', max_length=32, blank=False)
    avatar = models.ImageField('Аватар', upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

