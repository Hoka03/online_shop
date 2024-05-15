from apps.general.models import General
from apps.wishlists.models import Wishlist
from apps.general.models import PaymentMethod
from apps.carts.models import UserCart


def general(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user.pk).values_list('product_id', flat=True)
    generals = General.objects.all()
    general = generals.first()
    pay_methods = PaymentMethod.objects.all()
    cart_count = UserCart.objects.all().count()

    context = {
        'generals': generals,
        'wishlists': wishlists,
        'pay_methods': pay_methods,
        'shipping': int(general.shipping),
        'cart_count': cart_count
    }

    return context

