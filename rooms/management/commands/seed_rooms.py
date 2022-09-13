import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates fasilities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="룸을 몇개 만들건지?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                # https://faker.readthedocs.io/en/master/providers/baseprovider.html
                "name": lambda x: seeder.faker.company(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(100, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )

        created_photos = seeder.execute()

        # seed 생성된 데이터의 아이디 배열을 가져옴
        created_clean = flatten(list(created_photos.values()))

        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:

            # 배열의 아이디 마다 room 변수에 아이디 저장
            roomObj = room_models.Room.objects.get(pk=pk)  # pk > id, 프라이머리 키

            # 포토 데이터, 각 아이디 마다 3 ~ 10,30 만큼의 랜덤한 갯수의 생성
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=roomObj,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )

            # Many to Many filed
            # amenities 갯수 만큼 반복문 실행, 50확률로 amenities 추가
            for a in amenities:
                random_count = random.randint(1, 5)
                if random_count % 2 == 0:
                    roomObj.amenities.add(a)

            for f in facilities:
                random_count = random.randint(1, 5)
                if random_count % 2 == 0:
                    roomObj.facilities.add(f)

            for r in rules:
                random_count = random.randint(1, 5)
                if random_count % 2 == 0:
                    roomObj.house_rules.add(r)

        # 그냥 성공 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))

# > python manage.py seed_rooms --number 50
