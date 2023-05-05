from django.shortcuts import render


def display_home(request):
    return render(request, 'catalog/display_home.html')


def display_info(request):
    return render(request, 'catalog/display_info.html')
