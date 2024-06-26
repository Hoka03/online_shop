from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'address1', 'address2',
                    'country', 'region', 'district', 'zip_code')

    readonly_fields = ('last_login', 'date_joined', 'email',)

    fields = ('password', 'last_login', 'is_active', 'date_joined', 'email', 'first_name', 'last_name', 'phone_number',
              'address1', 'address2',
              'country', 'region', 'district', 'zip_code')

    def save_formset(self, request, obj, form, change):
        if obj.pk and CustomUser.objects.get('pk=obj.pk').password != obj.password:
            obj.set_password(obj.password)
        obj.save()

