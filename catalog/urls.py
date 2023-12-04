from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, categories


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('categories/', categories, name='categories'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail')
]
