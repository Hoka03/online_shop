from django.core.management import BaseCommand
from apps.general.models import General, Service, Banner, SocialLink, PaymentMethod, Coupon


class Command(BaseCommand):
    def handle(self, *args, **options):
        #General generate

        general = [
            General(name=f'name{1}',
                    phone_number=f'+{998999875421}',
                    email=f'tolqinovoybek@gmail.com',
                    address=f'Sergeli 8A',
                    desc=f'This magazine is very wonderful!!!', )
        ]
        General.objects.bulk_create(general)
        self.stdout.write(self.style.SUCCESS(f'{General.objects.count()} general created'))

        #Service Generate
        services = [
            Service(title_uz=f'title_uz{i}', slug=f'slug{i}', title_ru=f'title-ru{i}')
            for i in range(1, 7)
        ]
        Service.objects.bulk_create(services)
        self.stdout.write(self.style.SUCCESS(f'{Service.objects.count()} services created'))

        #Banners Generate
        banners = [
            Banner(sub_category_id=i,
                   title_uz=f'title_uz{i}',
                   slug=f'slug-{i}',
                   title_ru=f'title-ru{i}',
                   desc_uz=f'desc_uz{i}',
                   desc_ru=f'desc_ru{i}', )
            for i in range(1, 9)
        ]
        Banner.objects.bulk_create(banners)
        self.stdout.write(self.style.SUCCESS(f'{Banner.objects.count()} banners created'))

        #PaymentMethod Generate
        payment_methods = [
            PaymentMethod(name=f'NameNo{i}',
                          slug=f'slug-no{i}', )
            for i in range(1, 6)
        ]
        PaymentMethod.objects.bulk_create(payment_methods)
        self.stdout.write(self.style.SUCCESS(f'{PaymentMethod.objects.count()} payment_methods create'))

        #Coupon Generate
        coupon = [
            Coupon(title_uz=f'title_uz No{i}',
                   slug=f'slug-{i}',
                   title_ru=f'title_ru No{i}',
                   amount=f'{i+1.0}',
                   code=f'ABcd{i}',)
            for i in range(1, 10)
        ]
        Coupon.objects.bulk_create(coupon)
        self.stdout.write(self.style.SUCCESS(f'{Coupon.objects.count()} coupon create'))

        #SocialLinks Generate
        social_links = [
            SocialLink(name=f'name No{i}',
                       slug=f'slug-No{i}',
                       link=f'https://www.instagram.com/{i}', )
            for i in range(1, 5)
        ]
        SocialLink.objects.bulk_create(social_links)
        self.stdout.write(self.style.SUCCESS(f'{SocialLink.objects.count()} social_links create'))
