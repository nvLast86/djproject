from django.shortcuts import render
from .models import Category


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'catalog/contacts.html')


def categories(request):
    categories = Category.objects.order_by('pk')
    context = {'categories': categories}
    return render(request, 'catalog/categories.html', context)
