import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models
from reviews import models as review_models

name = "reviews"


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
            review_models.Review,
            number,
            {
                "reviews": lambda x: seeder.faker.text(max_nb_chars=80),
                "cleanliness": lambda x: random.randint(1, 5),
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
            },
        )

        seeder.execute()

        # 그냥 성공 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} {name} created!"))

# > python manage.py seed_reviews --number 50
