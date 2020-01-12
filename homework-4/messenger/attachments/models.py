from django.db import models

# Create your models here.


class Attachment(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True, related_name='attachments',
                             verbose_name='Чат')
    user = models.ForeignKey('user_profile.UserProfile', on_delete=models.SET_NULL, null=True,
                             related_name='attachments', verbose_name='Отправитель')
    message = models.ForeignKey('mymessages.Message', on_delete=models.SET_NULL, null=True,
                                related_name='attachments', verbose_name='Сообщение')
    type_attachment = models.CharField('Тип вложения', max_length=32, blank=True)
    url = models.CharField('Ссылка', max_length=256, blank=True)

    key = models.CharField('Ключ', max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
