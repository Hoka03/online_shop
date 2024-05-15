from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Avg

from apps.comments.forms import CommentCreateForm
from apps.products.models import Product
from apps.comments.models import Comment


def comment_page(request, product_id):
    user = request.user
    if request.method != 'POST':
        return redirect('product_detail_page', product_id)

    form = CommentCreateForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)

        comment.product_id = product_id
        if user.is_authenticated:
            comment.user, comment.name, comment.email = user, user.get_full_name(), user.email

        comment.save()
        messages.success(request, 'Comment SUCCESS Added!!!')
        avg_rating = Comment.objects.all().aggregate(avg=Avg('rating'))['avg']
        Product.objects.filter(pk=product_id).update(rating=avg_rating)
    else:
        messages.error(request, form.errors)

    return redirect('product_detail_page', product_id)

