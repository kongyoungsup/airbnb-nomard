from django.db import models
from core import models as core_models


class Review(core_models.TimeStampModel):

    """ Revires Model Definition"""

    reviews = models.TextField()
    cleanliness = models.IntegerField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name='reviews', on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reviews} - {self.room}'

    def rating_average(self):
        avg = (
            self.cleanliness +
            self.accuracy +
            self.communication +
            self.location +
            self.check_in +
            self.value
        ) / 6
        return round(avg, 2)

    # 모델 이름 변경
    rating_average.short_description = 'Avg.'
