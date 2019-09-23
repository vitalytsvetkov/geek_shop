from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot


def main(request):
    context = {'username': 'alexey'}
    return render(request, 'mainapp/main.html', context)


def products(request, pk=None):
    products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    if pk is not None:
        if pk > 0:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category=category)

        context = {'products': products, 'categories': ProductCategory.objects.all(), 'basket': basket}
        return render(request, 'mainapp/products.html', context)
    else:
        context = {
            'hot_product': Product.objects.filter(is_hot=True).first(),
            'categories': ProductCategory.objects.all(),
            'basket': basket
        }
        return render(request, 'mainapp/hot_product.html', context)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': request.user.basket.all(),
    }

    return render(request, 'mainapp/product.html', content)


def contacts(request):
    return render(request, 'mainapp/contacts.html')