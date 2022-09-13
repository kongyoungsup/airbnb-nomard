from django.db import models
from core import models as core_models


class List(core_models.TimeStampModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name='lists', on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def ___str___(self):
        return self.name

    def rooms_count(self):
        return self.rooms.count()

    rooms_count.short_description = 'Nember of rooms'
