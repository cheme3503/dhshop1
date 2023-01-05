from django.urls import path, re_path
from .views import *


app_name = 'shop'

urlpatterns = [
    path('', product_in_category, name='product_all'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]

