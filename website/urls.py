from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path("checkout/", checkout, name="checkout"),
    path("contact/", contact, name="contact"),
    path("detail/", detail, name="detail"),
    path("cart/", cart, name="cart"),
]