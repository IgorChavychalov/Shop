from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser


def index(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'админка/пользователи',
        'objects': users_list
    }
    return render(request, 'adminapp/index.html', context)

