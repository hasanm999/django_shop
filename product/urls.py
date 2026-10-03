from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.product_list, name="list"),
    path("<int:pk>/", views.product_detail, name="detail"),
    path("<int:pk>/rate/", views.rate_product, name="rate"),
]