from django.core.management.base import BaseCommand
from django_seed import Seed  # 장고 seed 호출
from users.models import User


class Command(BaseCommand):

    help = "This command creates Users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="몇명의 유저를 만들건가요"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(  # 제외 할 필드
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False
            }
        )
        seeder.execute()

        # 그냥 성공 메세지
        self.stdout.write(self.style.SUCCESS(
            f"{number} User created!"))

# > python manage.py seed_users --number 50
