from django.core.management import BaseCommand
from apps.comments.models import Comment
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        comments = [Comment(product_id=j.pk,
                            name=f'tolqinovoybek{i}',
                            email=f'tolqinovoybek{i}@gmail.com',
                            rating=f'{5}',
                            message=f'message{i}')
                    for i in range(1, 4)
                    for j in Product.objects.all()]
        Comment.objects.bulk_create(comments)
        self.stdout.write(self.style.SUCCESS(f'{Comment.objects.count()} comments created'))
