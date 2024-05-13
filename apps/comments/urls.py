from django.urls import path

from apps.comments.views import comment_page


urlpatterns = [
    path('add-comment/<int:product_id>/', comment_page, name='comment_page')
]