from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


# def detail(request):
#     return render(request, 'detail.html')

# def shop(request):
#     return render(request, 'shop_list.html')

# def cart(request):
#     return render(request, 'cart.html')