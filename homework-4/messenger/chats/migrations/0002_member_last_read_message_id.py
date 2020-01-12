# Generated by Django 2.2.5 on 2019-11-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mymessages', '0001_initial'),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_read_message_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mymessages.Message'),
        ),
    ]