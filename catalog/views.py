from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:catalog_list')


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:catalog_list')


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')


def display_info(request):
    return render(request, 'catalog/display_info.html')
