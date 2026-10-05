from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import RatingForm
from .models import Product, Rating


def product_list(request):

    query = request.GET.get("q", "").strip()

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    context = {
        "products": products,
        "query": query,
    }

    return render(
        request,
        "products/product_list.html",
        context
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    form = None

    if request.user.is_authenticated:
        existing = Rating.objects.filter(
            product=product,
            user=request.user
        ).first()

        form = RatingForm(instance=existing)

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "form": form
        }
    )


@login_required
@require_POST
def rate_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    existing = Rating.objects.filter(
        product=product,
        user=request.user
    ).first()

    form = RatingForm(
        request.POST,
        instance=existing
    )

    if form.is_valid():

        rating = form.save(commit=False)

        rating.product = product
        rating.user = request.user

        rating.save()

        messages.success(
            request,
            "Your rating has been saved."
        )

    else:

        messages.error(
            request,
            "Invalid rating."
        )

    return redirect(
        "product:detail",
        pk=pk
    )