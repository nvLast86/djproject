from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Version
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
        return Product.objects.filter(version__is_active=True)


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products-list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        subjectformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = subjectformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subjectformset(instance=self.object)
        return context_data


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog_change_product'
    success_url = reverse_lazy('catalog:product-detail')

    def get_success_url(self):
        return reverse('catalog:product-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        subjectformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = subjectformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subjectformset(instance=self.object)
        return context_data

    def has_permission(self):
        product = self.get_object()
        return product.has_permission_to_change(self.request.user)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:products-list')

    def has_permission(self):
        product = self.get_object()
        return product.has_permission_to_delete(self.request.user)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog/categories.html'


