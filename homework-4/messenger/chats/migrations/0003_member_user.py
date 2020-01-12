# Generated by Django 2.2.5 on 2019-11-05 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_member_last_read_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]