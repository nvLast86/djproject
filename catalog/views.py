from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView


# Create your views here.
def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)


