from django.urls import path

from apps.carts.views import add_cart, shop_coupon, update_count, delete_cart


urlpatterns = [
    path('add-cart/<int:product_id>/', add_cart, name='add_cart'),
    path('shop-cart/', shop_coupon, name='shop_coupon'),
    path('update-count/<int:pk>/', update_count, name='update_count'),
    path('delete-cart/<int:pk>/', delete_cart, name='delete_cart')
]