import random

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import ProductCategory, Product


# def get_basket(request):
#     if request.user.is_authenticated:
#         return request.user.basket.all()
#     else:
#         return []


def get_hot_product():
    return random.choice(Product.objects.filter(is_active=True, category__is_active=True))


def get_same_products(hot_product):
    # ограничемься выводом 4х товаров
    return hot_product.category.product_set.filter(is_active=True).exclude(pk=hot_product.pk)[:4]


def get_menu():
    return ProductCategory.objects.filter(is_active=True)


def index(request):
    context = {
        'title': 'главная',
        # 'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': 'каталог',
        'links_menu': get_menu(),
        # 'basket': get_basket(request),
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/catalog.html', context)


def category(request, pk, page=1):
    if int(pk) == 0:
        category = {
            'pk': 0,
            'name': 'все',
        }
        products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.filter(is_active=True).order_by('price')
        # альтернативный вариант
        # products = Product.objects.filter(category__pk=pk).order_by('price')
        # ограничение выдаваемых продуктов
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'title': 'продукты',
        'links_menu': get_menu(),
        # 'basket': get_basket(request),
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/product_list.html', context)


def product(request, pk):
    object = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(object)

    context = {
        'title': 'продукты',
        'links_menu': get_menu,
        # 'basket': get_basket(request),
        'object': object,
        'same_products': same_products,
    }
    return render(request, 'mainapp/product.html', context)


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
        'locations': locations,
        # 'basket': get_basket(request),
    }
    return render(request, 'mainapp/contacts.html', context)
