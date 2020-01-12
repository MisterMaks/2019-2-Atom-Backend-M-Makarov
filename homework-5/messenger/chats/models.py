from django.db import models
from stickers.models import Sticker

# Create your models here.

class Chat(models.Model):
    title = models.CharField(max_length=128, blank=False)
    sticker = models.ForeignKey(Sticker, on_delete=models.SET_NULL, null=True, related_name='chats')

