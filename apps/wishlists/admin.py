from django.contrib import admin

from apps.wishlists.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at',)
    list_display_links = list_display
