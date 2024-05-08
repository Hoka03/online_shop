from django.urls import path

from apps.orders.views import order_page


urlpatterns = [
    path('', order_page, name='checkout_page')
]