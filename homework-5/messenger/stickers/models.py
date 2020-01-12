from django.db import models

# Create your models here.

class Sticker(models.Model):
    name = models.CharField(max_length=32, null=True)
    description = models.TextField()
    is_default = models.BooleanField(default=True)

