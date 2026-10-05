from django.urls import path
from .views import *

app_name = "website"
urlpatterns = [
    path('', index, name='index'),
    # path('shop_list/', shop, name='shop_list'),
    path("checkout/", checkout, name="checkout"),
    path("contact/", contact, name="contact"),
    # path("detail/", detail, name="detail"),
    # path("cart/", cart, name="cart"),
]