from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("", views.order_list, name="list"),
    path("checkout/", views.checkout, name="checkout"),
    path("<int:pk>/", views.order_detail, name="detail"),
    path("<int:pk>/cancel/", views.cancel_order, name="cancel"),
]