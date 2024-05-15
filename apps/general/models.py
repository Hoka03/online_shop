from django.db import models
from django.core.validators import ValidationError
from django.utils.timezone import now

from apps.categories.models import SubCategory
from apps.users.valedate import validate_phone_number
from apps.comments.serveces import normalize_text
from apps.general.services import get_field_by_language


class General(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='general/logo', blank=True, null=True)
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
    email = models.EmailField()
    address = models.CharField(max_length=100)
    desc = models.CharField(max_length=500, blank=True)
    shipping = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

    def get_normalize_fields(self):
        return [
            'name',
            'address',
            'desc'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class Service(models.Model):
    title_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    title_ru = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(upload_to='general/service/image/%Y/%m/%d')

    def __str__(self):
        return self.title

    @property
    def title(self):
        return get_field_by_language(self, 'title')

    def get_normalize_fields(self):
        return [
            'title_uz',
            'title_ru'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class Banner(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    title_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    title_ru = models.CharField(max_length=50, blank=True)
    desc_uz = models.CharField(max_length=50)
    desc_ru = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    @property
    def title(self):
        return get_field_by_language(self, 'title')

    @property
    def desc(self):
        return get_field_by_language(self, 'desc')

    def get_normalize_fields(self):
        return [
            'title_uz',
            'title_ru',
            'desc_uz',
            'desc_ru'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_image/%Y/%m/%d')
    product = models.ForeignKey(Banner, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


class Coupon(models.Model):
    title_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    title_ru = models.CharField(max_length=50, blank=True)

    code = models.CharField(max_length=10, unique=True)
    from_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='So\'mda yoki foizda kiriting!!!')
    is_percent = models.BooleanField(default=True)

    @classmethod
    def check_coupon(cls, code: str):
        today = now().date()
        coupon = cls.objects.filter(code=code, from_date__gte=today, end_date__lte=today).first()
        if not coupon:
            return None
        return coupon.amount, coupon.is_percent

    def __str__(self):
        return self.title

    @property
    def title(self):
        return get_field_by_language(self, 'title')

    def clean(self):
        if self.is_percent and not (1 <= self.amount <= 100):
            raise ValidationError({'amount': '[1 : 100]-oraliqda kiriting!!!'})

    def get_normalize_fields(self):
        return [
            'title_uz',
            'title_ru'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        self.code = ''.join(self.code.split())
        super().save(*args, **kwargs)


class SocialLink(models.Model):
    icon = models.ImageField(upload_to='general/social_link/icon/')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    link = models.URLField()

    def __str__(self):
        return self.name

    def get_normalize_fields(self):
        return [
            'name',
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=35, unique=True)
    logo = models.ImageField(upload_to='general/payment_method/logo/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_normalize_fields(self):
        return [
            'name',
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)