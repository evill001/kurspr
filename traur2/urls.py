from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name = "home"),
    path('suvenir/', suvenir, name = "suvenir"),
    path('kontact/', kontact, name = "kontact"),
    path('reg/', reg, name = "reg"),
    path('vhod/', vhod, name = "vhod"),
    path('product_detail/', product_detail, name = "product_detail"),
    path('cart/', cart, name = "cart"),
    path('product_detail2/', product_detail2, name = "product_detail2"),
]
    