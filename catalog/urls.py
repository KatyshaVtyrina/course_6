from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import display_info, CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, \
    CatalogDeleteView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('products/<int:pk>/', CatalogDetailView.as_view(), name='product_item'),
    path('products/create/', CatalogCreateView.as_view(), name='catalog_create'),
    path('products/update/<int:pk>/', CatalogUpdateView.as_view(), name='catalog_update'),
    path('products/delete/<int:pk>/', CatalogDeleteView.as_view(), name='catalog_delete'),
    path('contacts/', display_info),
]
