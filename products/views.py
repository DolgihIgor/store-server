from django.shortcuts import render


def index(request):
    """ Контроллер для главной страницы """
    return render(request, 'products/index.html')


def products(request):
    """ Контроллер для страницы с товарами """
    return render(request, 'products/products.html')