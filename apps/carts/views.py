from django.shortcuts import redirect, render
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.general.models import General

from apps.features.models import ProductFeature
from apps.carts.models import UserCart
from apps.general.models import Coupon


@login_required(login_url='/users/login_page/')
def add_cart(request, product_id):
    user = request.user

    if request.method != 'POST':
        return redirect('product_detail_page', product_id)

    counts = request.POST.get('counts', 1)

    features = [
        int(request.POST[feature])
        for feature in request.POST if feature.startswith('feature_')]
    product_features = ProductFeature.objects.annotate(count=Count('feature_values')).filter(product_id=product_id,
                                                                                             count=len(features))
    for feature_value_id in features:
        product_features = product_features.filter(feature_values__id=feature_value_id)

    if product_features:
        user_cart, created = UserCart.objects.get_or_create(product_feature_id=product_features.first().pk,
                                                            user_id=user.pk)
        if created:
            user_cart.counts = int(counts)
            user_cart.save()
            messages.success(request, 'successfully added to cart.')
        else:
            messages.error(request, 'This product was already added')
    else:
        messages.error(request, 'This field does not exist')

    return redirect('product_detail_page', product_id)


@login_required
def update_count(request, pk):
    if request.method != 'POST':
        return redirect('shop_coupon')
    counts = request.POST.get('counts')

    cart = UserCart.objects.get(pk=pk)
    quant = cart.product_feature.quantity

    if int(counts) > quant:
        messages.error(request, f'Here products a lot')
    else:
        cart.counts = counts
        cart.save()
        messages.success(request, 'Successfully added')

    return redirect('shop_coupon')


@login_required
def delete_cart(request, pk):
    obj = UserCart.objects.get(pk=pk)
    if obj:
        obj.delete()
    return redirect('shop_coupon')


def shop_coupon(request):
    user = request.user
    carts = UserCart.objects.filter(user=user).select_related('product_feature')
    total = sum(cart.product_feature.price * cart.counts for cart in carts)
    shipping = General.objects.all()
    ctx = {
        'carts': carts,
        'total': total,
        'shipping': shipping
    }

    coupon_code = request.POST.get('coupon_code')
    if coupon_code:
        coupon = Coupon.check_coupon(coupon_code)
        if coupon:
            ctx['coupon'] = coupon
            messages.success(request, 'Your coupon has been activated.')
        else:
            messages.error(request, 'Coupon code is not valid')

    return render(request, 'shop_cart.html', ctx)

