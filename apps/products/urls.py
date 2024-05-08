from django.urls import path

from apps.products.views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product-list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail_page'),
]
