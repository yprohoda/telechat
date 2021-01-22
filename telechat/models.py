from datetime import datetime

from django.db import models


class Chat(models.Model):
    user_id = models.CharField(default=0, max_length=100)
    user_nick = models.CharField(default=0, max_length=100)
    chat_id = models.CharField(default=0, max_length=100)
    manager_id = models.CharField(default=0, max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)

    # def __str__(self):
    #     return self.user_id, self.user_nick, self.chat_id, self.manager_id

    def get_chat_id(self):
        return self.chat_id