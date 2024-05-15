from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.contrib import messages

from apps.carts.models import UserCart
from apps.orders.forms import OrderForm
from apps.general.models import PaymentMethod


@login_required
def checkout_page(request):
    pay_methods = PaymentMethod.objects.all()
    user = request.user
    user_carts = UserCart.objects.filter(user=user)
    subtotal = UserCart.objects.filter(user=user).aggregate(s=Sum(F('product_feature__price') * F('counts'),
                                                                  default=0))['s']
    context = {
        'user_carts': user_carts,
        'subtotal': subtotal,
        'pay_methods': pay_methods
    }
    return render(request, 'checkout.html', context)


@login_required
def order(request):
    if request.method != 'POST':
        return redirect('checkout_page')
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
        print('success')
        messages.success(request, 'Successfully.')
    else:
        messages.error(request, form.errors)
        print(form.errors)
    return redirect('checkout_page')





