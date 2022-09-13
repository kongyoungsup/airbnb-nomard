from ntpath import join
from django.db import models
import conversations
from core import models as core_models


class Conversation(core_models.TimeStampModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name='conversations', blank=True)

    # def __str__(self):
    #     return str(self.created)  # 스트링으로 바꿈

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "메시지 수"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "대화인원"


class Message(core_models.TimeStampModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name='messages', on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "Conversation", related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
