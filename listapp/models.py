from django.db import models
from datetime import datetime, timedelta

class Item(models.Model):
    name = models.CharField(max_length=80)
    purchased = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
