from xmlrpc.client import boolean
from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservetions(core_models.TimeStampModel):

    STATUS_PENDING = "pending"
    STATUS_COMFIRMES = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "PENDING"),
        (STATUS_COMFIRMES, "COMFIRMES"),
        (STATUS_CANCELED, "CANCELED"),
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    check_in = models.DateField()
    check_out = models.DateField()
    geust = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
