from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = [CustomUser(email=f'email{i}@gmail.com',
                            password=f'password{i}',
                            first_name=f'first_name{i}',
                            last_name=f'last_name{i}',
                            phone_number=f'+{998999632154}',
                            )
                 for i in range(1, 1000)]
        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('1000 users created'))
