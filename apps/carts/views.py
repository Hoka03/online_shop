from django.shortcuts import redirect, render

from apps.features.models import ProductFeature
from apps.carts.models import UserCart


def add_cart(request, product_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('login-page')

    counts = request.POST.get('counts', 1)
    features = [
        int(request.POST[feature])
        for feature in request.POST if feature.startswith('feature_')]
    print(features)
    product_feature = ProductFeature.objects.filter(product_id=product_id,
                                                    feature_value__id__in=features).first()

    if product_feature:
        UserCart.objects.create(product_feature_id=product_feature.pk,
                                user_id=user.pk, counts=int(counts))
    return redirect(request.META['HTTP_REFERER'])


def shop_cart(request):
    return render(request, 'shop_cart.html')