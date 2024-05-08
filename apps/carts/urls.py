from django.urls import path

from apps.carts.views import cart_page


urlpatterns = [
    path('', cart_page, name='cart-page')
]