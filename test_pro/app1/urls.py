from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('catalog/', catalog, name='catalog'),
    path('compare/', compare, name='compare'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
]
