import os

from django.core.management import BaseCommand
from apps.general.models import General, Service, Banner, SocialLink, PaymentMethod, Coupon


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system('rm -rf db.sqlite3')
        self.stdout.write(self.style.SUCCESS('makemigrations'))
        os.system('python manage.py makemigrations')
        self.stdout.write(self.style.SUCCESS('migrate'))
        os.system('python manage.py migrate')
        self.stdout.write(self.style.SUCCESS('generate_users'))
        os.system('python manage.py generate_users')
        self.stdout.write(self.style.SUCCESS('generate_categories'))
        os.system('python manage.py generate_categories')
        self.stdout.write(self.style.SUCCESS('generate_contacts'))
        os.system('python manage.py generate_contacts')
        self.stdout.write(self.style.SUCCESS('generate_products'))
        os.system('python manage.py generate_products')
        self.stdout.write(self.style.SUCCESS('generate_general'))
        os.system('python manage.py generate_general')
        self.stdout.write(self.style.SUCCESS('generate_comments'))
        os.system('python manage.py generate_comments')
        self.stdout.write(self.style.SUCCESS('generate_features'))
        os.system('python manage.py generate_features')


