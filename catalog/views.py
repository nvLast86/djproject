from django.shortcuts import render
from .models import Product, Category
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'catalog/home.html'
    extra_context = { 'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'catalog/contacts.html')


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog/categories.html'


