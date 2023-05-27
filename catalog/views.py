from django.shortcuts import render
from catalog.models import Product


def display_home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог',
    }
    return render(request, 'catalog/display_home.html', context)


def display_info(request):
    return render(request, 'catalog/display_info.html')
