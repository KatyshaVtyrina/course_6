from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['name'] = self.get_object()
        context_data['description'] = self.get_object()
        context_data['versions'] = Version.objects.filter(product=self.object, is_active=True)
        return context_data


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form_with_formset.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:catalog_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')


class VersionListView(ListView):
    model = Version


def display_info(request):
    return render(request, 'catalog/display_info.html')
