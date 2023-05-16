from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import display_home, display_info


app_name = CatalogConfig.name

urlpatterns = [
    path('', display_home),
    path('contacts/', display_info),
]
