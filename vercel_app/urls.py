# vercel-django-example/example/urls.py
# https://github.com/jayhale/vercel-django-example/blob/main/example/urls.py#L7

from django.urls import path
from example.views import *

urlpatterns = [
    path('', index),
    path('chess', chess),
]