from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from product.models import Product
from .forms import MAX_QUANTITY, QuantityForm
from .models import Cart, CartItem


def _redirect_back(request, default):
    next_url = request.POST.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)
    return redirect(default)


@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product")
    return render(request, "carts/cart_detail.html", {"cart": cart, "items": items})


@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity}
        )
        if not created:
            item.quantity = min(item.quantity + quantity, MAX_QUANTITY)
            item.save(update_fields=["quantity"])
        messages.success(request, f"{quantity} x {product.name} added to your cart.")
    else:
        messages.error(request, f"Quantity must be a number between 1 and {MAX_QUANTITY}.")
    return _redirect_back(request, "cart:detail")


@login_required
@require_POST
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    form = QuantityForm(request.POST)
    if form.is_valid():
        item.quantity = form.cleaned_data["quantity"]
        item.save(update_fields=["quantity"])
        messages.success(request, "Cart updated.")
    else:
        messages.error(request, f"Quantity must be a number between 1 and {MAX_QUANTITY}.")
    return redirect("cart:detail")


@login_required
@require_POST
def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect("cart:detail")