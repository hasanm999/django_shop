from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from cart.models import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = list(cart.items.select_related("product")) if cart else []
    if not items:
        messages.error(request, "Your cart is empty.")
        return redirect("cart:detail")

    total = sum(item.total_price for item in items)

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                order.user = request.user
                order.total_price = total
                order.save()
                OrderItem.objects.bulk_create(
                    [
                        OrderItem(
                            order=order,
                            product=item.product,
                            product_name=item.product.name,
                            price=item.product.price,
                            quantity=item.quantity,
                        )
                        for item in items
                    ]
                )
                cart.items.all().delete()
            messages.success(request, "Your order has been placed.")
            return redirect("order:detail", pk=order.pk)
    else:
        form = CheckoutForm(initial={"full_name": request.user.get_full_name()})

    return render(request, "orders/checkout.html", {"form": form, "items": items, "total": total})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order.objects.prefetch_related("items"), pk=pk, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})


@login_required
@require_POST
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if order.status == Order.Status.PENDING:
        order.status = Order.Status.CANCELED
        order.save(update_fields=["status"])
        messages.success(request, "Your order has been canceled.")
    else:
        messages.error(request, "Only pending orders can be canceled.")
    return redirect("order:detail", pk=pk)