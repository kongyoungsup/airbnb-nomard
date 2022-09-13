from django.core.management.base import BaseCommand
# (or) from rooms import models as room_models
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates fasilities"

    def handle(self, *args, **options):
        fasilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in fasilities:
            Facility.objects.create(name=a)

        # 그냥 성공 메세지
        self.stdout.write(self.style.SUCCESS(
            f"{len(fasilities)} Facility created!"))

# > python manage.py seed_fasilities
