import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models
from reservations import models as reservation_models

name = "reservations"


class Command(BaseCommand):

    help = f"This command creates {name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help=f"{name} 몇개 만들건지?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservetions,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "geust": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
                "check_in": lambda x: datetime.now() + timedelta(days=random.randint(-2, 2)),
                "check_out": lambda x: datetime.now() + timedelta(days=random.randint(3, 10))
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {name} created!"))


# > python manage.py seed_reservations --number 50
