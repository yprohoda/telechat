from datetime import datetime

from django.db import models

class Chat(models.Model):
    user_id = models.CharField(default=0, max_length=100)
    chat_id = models.CharField(default=0, max_length=100)
    manager_id = models.CharField(default=0, max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.chat_id