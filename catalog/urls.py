from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import (contacts, ProductListView, ProductDetailView, CategoryListView, HomeView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:id>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDeleteView.as_view(), name='delete'),
    ]
