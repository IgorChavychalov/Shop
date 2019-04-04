from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
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

    return render(request, 'mainapp/catalog.html', context)


def category(request, pk):
    # links_menu = ProductCategory.objects.all()

    if int(pk) == 0:
        products = Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        # products = Product.objects.filter(category__pk=pk).order_by('price')
        products = category.product_set.order_by('price')

    content = {
        'title': 'продукты',
        # 'links_menu': links_menu,
        'category': category,
        'products': products,
    }

    return render(request, 'mainapp/products_list.html', content)


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
