from django.urls import path
from apps.wishlists.views import product_wishlists, wishlist

urlpatterns = [
    path('product_wishlists/<int:pk>', product_wishlists, name='product_wishlists_page'),
    path('', wishlist, name='wishlist-page')
]