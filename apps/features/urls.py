from django.urls import path

from apps.features.views import feature_list


patterns = [
    path('feature-list/', feature_list, name='feature_list')
]