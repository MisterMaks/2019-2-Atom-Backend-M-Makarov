# Generated by Django 2.2.5 on 2019-11-12 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20191106_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='chats.Chat', verbose_name='Чат'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_read_message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mymessages.Message', verbose_name='Последнее прочитанное сообщение'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
