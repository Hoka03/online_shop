from django.contrib import admin
from apps.general.models import General, Service, Banner, SocialLink,  PaymentMethod, Coupon, BannerImage


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'phone_number', 'email', 'address', 'desc')
    list_display_links = list_display

    def has_add_permission(self, request):
        return not General.objects.last()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'slug', 'title_ru', 'icon',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title_uz']}


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'slug', 'title_ru', 'code', 'from_date', 'end_date', 'amount', 'is_percent',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title_uz']}


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'slug', 'link',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'logo',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


class BannerImageInline(admin.TabularInline):
    model = BannerImage


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('sub_category', 'title_uz', 'slug', 'title_ru', 'desc_uz', 'desc_ru',)
    prepopulated_fields = {'slug': ['title_uz']}
    inlines = [BannerImageInline]


