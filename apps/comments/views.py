from django.shortcuts import render, redirect
from django.contrib import messages

from apps.comments.forms import CommentCreateForm


def comment_page(request, pk):
    if request.method != 'POST':
        return render(request, 'product_detail.html')

    form = CommentCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(request.META['HTTP_REFERER'])


    # user = request.user
    #
    # rating = request.POST.get('rating')
    # message = request.POST.get('message')
    # name = request.POST.get('name')
    # email = request.POST.get('email')
    #
    # if request.user.is_authenticated:
    #     name = user.first_name
    #     email = user.email
    # elif not (name and email):
    #     messages.error(request, 'Name or Email was not entered!!!')
    #     return redirect('product_detail_page')
    #
    # Comment.objects.create(name=name, email=email, rating=rating, message=message)
    #
    # messages.SUCCESS(request, 'Comment placed SUCCESSFULLY')
    # return redirect('product_detail_page')