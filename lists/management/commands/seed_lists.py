import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models
from lists import models as list_models

name = "lists"


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
        # all_rooms = room_models.Room.objects.all()[4:10] // 4~10 번 까지
        seeder.add_entity(
            list_models.List,
            number,
            {
                "name": lambda x: seeder.faker.text(max_nb_chars=20),
                "user": lambda x: random.choice(all_users),
            },
        )

        created_reviews = seeder.execute()

        created_clean = flatten(list(created_reviews.values()))

        for pk in created_clean:

            listsObj = list_models.List.objects.get(pk=pk)  # pk > id, 프라이머리 키
            random_count = all_rooms[random.randint(
                0, 5): random.randint(6, 30)]  # all_rooms[5 : 30], 배열 5 에서 30까지
            listsObj.rooms.add(*random_count)

        # 그냥 성공 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} {name} created!"))

# > python manage.py seed_lists --number 50
