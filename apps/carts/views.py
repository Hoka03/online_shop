from django.shortcuts import redirect, render
from django.db.models import Count
from django.contrib import messages

from apps.features.models import ProductFeature
from apps.carts.models import UserCart
from apps.general.models import Coupon


def add_cart(request, product_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('login-page')

    if request.method != 'POST':
        return redirect('product_detail_page')

    counts = request.POST.get('counts', 1)
    features = [
        int(request.POST[feature])
        for feature in request.POST if feature.startswith('feature_')]
    product_features = ProductFeature.objects.filter(product_id=product_id,
                                                     feature_values__id__in=features
                                                     ).annotate(s=Count('feature_values')).order_by('s').last()
    if product_features:
        UserCart.objects.create(product_feature_id=product_features.pk,
                                user_id=user.pk, counts=int(counts))
    return redirect(request.META['HTTP_REFERER'])


def add_cart_shop(request, pk):
    if request.method != 'POST':
        return redirect('product_detail')

    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

    try:
        product = ProductFeature.objetcs.filter(product_id=pk)
    except ProductFeature.DoesNotExist:
        messages.error(request, 'Product does not exist')
        return redirect('product_detail')

    carts = request.session.get('cart', {})
    if product_id in carts:
        carts[product_id] += quantity
    else:
        carts[product_id] = quantity

    request.session['carts'] = carts
    messages.success(request, 'Product added to cart successfully')

    context = {
        'product': product,
        'carts': carts
    }
    return render(request, 'shop_cart.html', context)


def shop_coupon(request):
    context = {}
    coupon_code = request.POST.get('coupon_code')
    if coupon_code:
        coupon = Coupon.check_coupon(coupon_code)
        if coupon:
            context['coupon'] = coupon
            messages.success(request, 'Your coupon has been activated.')
        else:
            messages.error(request, 'Coupon code is not valid')

    return render(request, 'shop_cart.html', context)
