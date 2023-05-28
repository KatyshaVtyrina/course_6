from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import display_info, CatalogListView, CatalogDetailView, CatalogCreateView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('products/<int:pk>/', CatalogDetailView.as_view(), name='product_item'),
    path('products/create/', CatalogCreateView.as_view(), name='catalog_create'),
    path('contacts/', display_info),
]
