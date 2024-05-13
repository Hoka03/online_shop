from django.core.management import BaseCommand
from apps.categories.models import MainCategory, SubCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        main_cats = [
            MainCategory(name_uz='Electronics',
                         slug='electronics',
                         name_ru='Электроника'),

            MainCategory(name_uz='Clothing',
                         slug='clothing',
                         name_ru='Одежда'),

            MainCategory(name_uz='Books',
                         slug='books',
                         name_ru='Книги'),
        ]
        MainCategory.objects.bulk_create(main_cats)
        self.stdout.write(self.style.SUCCESS(f'{MainCategory.objects.count()} main_cats created'))

        sub_cats = [
            SubCategory(
                main_category_id=1,
                name_uz='Phones',
                slug=f'phones',
                name_ru='телефоны'
            ),
            SubCategory(
                main_category_id=1,
                name_uz='Laptops',
                slug=f'laptops',
                name_ru='ноутбукы'
            ),
            SubCategory(
                main_category_id=1,
                name_uz='TV',
                slug=f'tv',
                name_ru='телевизор'
            ),
            SubCategory(
                main_category_id=2,
                name_uz='Hoodies',
                slug=f'hoodies',
                name_ru='худи'
            ),
            SubCategory(
                main_category_id=2,
                name_uz='Sneakers',
                slug=f'sneakers',
                name_ru='красовки'
            ),
            SubCategory(
                main_category_id=2,
                name_uz='Sweater',
                slug=f'sweater',
                name_ru='кофта'
            ),
            SubCategory(
                main_category_id=3,
                name_uz='Phantasy',
                slug=f'phantasy',
                name_ru='фантастика'
            ),
            SubCategory(
                main_category_id=3,
                name_uz='Romance',
                slug=f'romance',
                name_ru='романы'
            ),
            SubCategory(
                main_category_id=3,
                name_uz='Historical',
                slug=f'historical',
                name_ru='историческый'
            ),
        ]
        SubCategory.objects.bulk_create(sub_cats)
        self.stdout.write(self.style.SUCCESS(f'{SubCategory.objects.count()} subcategory created!'))


        # sub_category_count = 0
        # for main_cat in main_cats:
        #     sub_cats.append(SubCategory(main_category_id=main_cat.pk,
        #                                 name_uz=f'{main_cat.name_uz} Phone',
        #                                 slug=f'{main_cat.slug}-phone-1',
        #                                 name_ru=f'{main_cat.name_ru} Телефон 1'))
        #     sub_cats.append(SubCategory(main_category_id=main_cat.pk,
        #                                 name_uz=f'{main_cat.name_uz} Subcategory 2',
        #                                 slug=f'{main_cat.slug}-subcategory-2',
        #                                 name_ru=f'{main_cat.name_ru} Subcategory 2'))
        #     sub_cats.append(SubCategory(main_category_id=main_cat.pk,
        #                                 name_uz=f'{main_cat.name_uz} Subcategory 3',
        #                                 slug=f'{main_cat.slug}-subcategory-3',
        #                                 name_ru=f'{main_cat.name_ru} Subcategory 3'))
        #     sub_category_count += 3
        #
        # SubCategory.objects.bulk_create(sub_cats)
        # self.stdout.write(self.style.SUCCESS(f'{sub_category_count} sub-categories created'))
