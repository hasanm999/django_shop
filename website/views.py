from django.shortcuts import render
from product.models import Product

# Create your views here.



def index(request):
    recent_products = Product.objects.order_by('-id')[:10]

    context = {
        'recent_products': recent_products,
    }

    return render(request, 'index.html', context)

# def checkout(request):
#     return render(request, 'checkout.html')



# def detail(request):
#     return render(request, 'detail.html')

# def shop(request):
#     return render(request, 'shop_list.html')

# def cart(request):
#     return render(request, 'cart.html')