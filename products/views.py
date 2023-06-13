from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    """ Контроллер для главной страницы """
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    """ Контроллер для страницы с товарами """
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)