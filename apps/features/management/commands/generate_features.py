from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        features = [
            Feature(
                main_category_id=1,
                ordering_number=1,
                name_uz='RAM',
                slug='ram',
                name_ru='ОЗУ'),

            Feature(
                main_category_id=2,
                ordering_number=2,
                name_uz='size',
                slug='size',
                name_ru='размер',
            ),

            Feature(
                main_category_id=3,
                ordering_number=3,
                name_uz='Genre',
                slug='genre',
                name_ru='Жанр'
            )
        ]
        Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS(f'{Feature.objects.count()} feature created!'))

        feature_value = [
            #ELECTRONICS
            FeatureValue(
                feature_id=1,
                value_uz='64GB',
                slug='64-gb',
                value_ru=f'64ГБ'
            ),
            FeatureValue(
                feature_id=1,
                value_uz='128GB',
                slug='128-gb',
                value_ru=f'128ГБ'
            ),
            FeatureValue(
                feature_id=1,
                value_uz='30',
                slug='30',
                value_ru='30'
            ),
            #CLOTHES
            FeatureValue(
                feature_id=2,
                value_uz='L',
                slug='l',
                value_ru='Л'
            ),
            FeatureValue(
                feature_id=2,
                value_uz='XL',
                slug='xl',
                value_ru='XЛ'
            ),
            FeatureValue(
                feature_id=2,
                value_uz='XXL',
                slug='xxl',
                value_ru='ХХЛ'
            ),

            #BOOKS
            FeatureValue(
                feature_id=3,
                value_uz='Phantasy',
                slug='phantasy',
                value_ru=f'Фантастика'
            ),
            FeatureValue(
                feature_id=3,
                value_uz='Romance',
                slug='romance',
                value_ru=f'романтика'
            ),
            FeatureValue(
                feature_id=3,
                value_uz='Historical',
                slug='historical',
                value_ru=f'Историческый'
            ),
        ]
        FeatureValue.objects.bulk_create(feature_value)
        self.stdout.write(self.style.SUCCESS(f'{FeatureValue.objects.count()} feature_value created'))
