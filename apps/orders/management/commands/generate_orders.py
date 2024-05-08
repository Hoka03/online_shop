from django.core.management import BaseCommand

from apps.orders.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        #Order Generate
        # last_order = Order.objects.order_by('-id').first()
        # last_order_id = last_order.pk if last_order else 1
        # if not Order.objects.exists():
        #     for i in range(20):
        #         order_obj = Order.objects.create(
        #             user_id=i,
        #             payment_method_id=i,
        #             coupon_code=i,
        #             coupon_amount=i,
        #             coupon_percent=i
        #         )
        #
        #         OrderItem.objects.bulk_create(
        #             [OrderItem(order=order_obj.pk,
        #                        product_feature=order_obj.pk,
        #                        counts=f'OrderItme No {j + 1}')
        #              for j in range(5)]
        #         )
            self.stdout.write(self.style.SUCCESS('100 Orders created'))

