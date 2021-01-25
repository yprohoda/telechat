from datetime import datetime

from django.db import models

class Chat(models.Model):
    user_id = models.TextField(default=0)
    chat_id = models.TextField(default=0)
    manager_id = models.TextField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.chat_id