# Generated by Django 2.2.5 on 2019-11-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0006_auto_20191127_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='key',
            field=models.CharField(blank=True, max_length=128, verbose_name='Ключ'),
        ),
    ]