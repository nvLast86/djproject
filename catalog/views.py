from django.shortcuts import render
from .models import Product, Category, Version
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm, VersionForm
from django.forms import inlineformset_factory


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

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        subjectformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = subjectformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subjectformset(instance=self.object)
        return context_data


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        subjectformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = subjectformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subjectformset(instance=self.object)
        return context_data


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog/categories.html'


