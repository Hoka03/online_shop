from django.urls import path

from apps.carts.views import add_cart, shop_cart


urlpatterns = [
    path('add-cart/<int:product_id>/', add_cart, name='add_cart'),
    path('shop-cart/', shop_cart, name='shop_cart')
]