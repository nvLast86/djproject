from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import (contacts, ProductListView, ProductDetailView, CategoryListView, HomeView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', cashe_page(60)(HomeView.as_view()), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', cashe_page(60)(CategoryListView.as_view()), name='categories'),
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/<int:pk>/', cashe_page(60)(ProductDetailView.as_view()), name='product-detail'),
    path('create/', never_cashe(ProductCreateView.as_view()), name='product-create'),
    path('update/<int:pk>/', never_cashe(ProductUpdateView.as_view()), name='product-update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
]
