# Generated by Django 2.2.5 on 2019-11-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0007_auto_20191127_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.CharField(blank=True, max_length=128, verbose_name='Ссылка'),
        ),
    ]