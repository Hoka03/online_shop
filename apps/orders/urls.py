from django.urls import path

from apps.orders.views import checkout_page, order


urlpatterns = [
    path('check-page/', checkout_page, name='checkout_page'),
    path('order-page/', order, name='order'),
]