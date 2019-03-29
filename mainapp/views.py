from django.shortcuts import render, HttpResponseRedirect
from mainapp.models import ProductCategory, Product
from django.urls import reverse


# обязательно указывать request!!!
def index(request):
    context = {
        'page_title': 'главная'
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):
    products = Product.objects.all()
    context = {
        'page_title': 'каталог',
        'products': products
    }

    return render(request, 'mainapp/catalog/catalog.html', context)


def category(request, pk):
    print(f'выбрали {pk}')

    # return HttpResponseRedirect('/products/')
    return HttpResponseRedirect(reverse('main:catalog'))

def contacts(request):
    locations = [
        {
            'city': 'Тихвин',
            'phone': '+7-999-999-99-99',
            'email': 'ppppp@mail.ru',
            'address': 'Тихвинская улица, 1',
        },
        {
            'city': 'Тихвин',
            'phone': '+7-888-888-88-88',
            'email': 'rrrrrr@mail.ru',
            'address': 'Тихвинская улица, 2',
        }
    ]
    context = {
        'page_title': 'контакты',
        'locations': locations
    }

    return render(request, 'mainapp/contacts.html', context)
