from django.db import models
from user_profile.models import UserProfile
# from messages.models import Message

# Create your models here.


class Chat(models.Model):
    is_group_chat = models.BooleanField('Групповой чат', default=False)
    topic = models.CharField('Тема', max_length=32, blank=True)
    last_message = models.OneToOneField('mymessages.Message', on_delete=models.SET_NULL, null=True,
                                        related_name='chat_last_message', verbose_name='Последнее сообщение')
    avatar = models.ImageField('Аватар чата', upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Member(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='members',
                             verbose_name='Пользователь')
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, related_name='members', verbose_name='Чат')

    new_messages = models.IntegerField('Новые сообщения', blank=True, null=True)  # число
    last_read_message = models.ForeignKey('mymessages.Message', on_delete=models.SET_NULL, null=True,
                                          related_name='members', verbose_name='Последнее прочитанное сообщение')

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чата'

