from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from apps.products.models import Product


def product_list(request):
    products = Product.objects.all().order_by('-id')

    selected_cat_id = request.GET.get('sub_category', '0')

    query = request.GET.get('query', '')
    if query != '':
        request.session['query'] = query
    else:
        request.session['query'] = ''

    if request.session.get('query'):
        products = products.filter(Q(title_uz__icontains=query) |
                                   Q(title_ru__icontains=query) |
                                   Q(short_desc_uz__icontains=query) |
                                   Q(short_desc_ru__icontains=query) |
                                   Q(long_desc_uz__icontains=query) |
                                   Q(long_desc_ru__icontains=query))

    if str(selected_cat_id).isdigit():
        selected_cat_id = int(selected_cat_id)
        if selected_cat_id != 0:
            request.session['selected_cat_id'] = selected_cat_id
        else:
            if request.session.get('selected_cat_id'):
                del request.session['selected_cat_id']

    page = request.GET.get('page', '1')
    paginator = Paginator(products, 9)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, template_name='products/product_detail.html', context=context)
