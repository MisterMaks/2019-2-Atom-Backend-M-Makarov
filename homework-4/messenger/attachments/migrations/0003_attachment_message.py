# Generated by Django 2.2.5 on 2019-11-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mymessages', '0001_initial'),
        ('attachments', '0002_attachment_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachments', to='mymessages.Message'),
        ),
    ]