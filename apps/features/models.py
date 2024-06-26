from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from apps.general.services import get_field_by_language
from apps.categories.models import MainCategory, SubCategory
from apps.comments.serveces import normalize_text


class Feature(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, blank=True, null=True)

    ordering_number = models.PositiveSmallIntegerField(unique=True)
    name_uz = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    name_ru = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return get_field_by_language(self, 'name')

    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('MainCategory yoki SubCategorydan birini tanlang')

    def get_category(self):
        return self.main_category or self.sub_category

    def get_normalize_fields(self):
        return [
            'name_uz',
            'name_ru',
        ]

    class Meta:
        verbose_name_plural = ' Features'

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='feature_value')
    value_uz = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    value_ru = models.CharField(max_length=70, blank=True)

    @property
    def value(self):
        return get_field_by_language(self, 'value')

    def __str__(self):
        return f'{self.feature}: {self.value}'

    class Meta:
        unique_together = ('feature', 'value_uz')

    def get_normalize_fields(self):
        return [
            'value_uz',
            'value_ru'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class ProductFeature(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='features')
    feature_values = models.ManyToManyField(FeatureValue, related_name='product_feature')
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)],
                                help_text='So\'mda kiriting')
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.product}'
