# Generated by Django 2.2.5 on 2019-11-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_auto_20191112_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='new_messages',
            field=models.IntegerField(blank=True, null=True, verbose_name='Новые сообщения'),
        ),
    ]
