from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    basket_items = request.user.basket.order_by('product__category')

    content = {
        'title': 'корзина',
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/index.html', content)


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()
    # альтернативный вариант
    # basket = request.user.basket.filter(product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    get_object_or_404(Basket, pk=pk).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
