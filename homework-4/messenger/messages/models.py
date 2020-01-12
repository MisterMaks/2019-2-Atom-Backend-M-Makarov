from django.db import models

# Create your models here.


class Message(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True, related_name='messages',
                             verbose_name='Чат')
    user = models.ForeignKey('user_profile.UserProfile', on_delete=models.SET_NULL, null=True,
                             related_name='messages', verbose_name='Отправитель')
    content = models.CharField('Текст', max_length=128, blank=False)
    added_at = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ['-added_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'



