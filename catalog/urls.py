from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories')
]
