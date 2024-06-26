from django.core.management import BaseCommand

from apps.carts.models import UserCart


class Command(BaseCommand):
    def handle(self, *args, **options):
        carts = [
            UserCart(
                user_id=f'user_{i}',
                product_id=f'product_{i}',
                counts=f'count-{i}',
            )
            for i in range(1, 11)
        ]
        UserCart.objects.bulk_create(carts)
        self.stdout.write(self.style.SUCCESS('10 carts create!!!'))