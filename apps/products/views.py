from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Min

from apps.products.models import Product
from apps.features.models import Feature
from apps.comments.models import Comment


def product_list(request):
    products = Product.objects.filter(features__isnull=False).distinct().order_by('-id')

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
            products = products.filter(sub_category_id=selected_cat_id)
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
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return redirect('product-list')

    images = product.productimage_set.order_by('ordering_number')
    price = product.features.aggregate(Min('price'))['price__min']
    product.price = price
    features = Feature.objects.filter(featurevalue__productfeature__product_id=product.pk).distinct()

    comments = Comment.objects.order_by('-id')[:10]

    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 4)
    page_obj = paginator.get_page(page)

    context = {
        'product': product,
        'images': images,
        'features': features,
        'page_obj': page_obj
    }
    return render(request, 'products/product_detail.html', context)


