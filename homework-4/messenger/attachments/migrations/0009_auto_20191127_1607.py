# Generated by Django 2.2.5 on 2019-11-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0008_auto_20191127_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.CharField(blank=True, max_length=256, verbose_name='Ссылка'),
        ),
    ]
