from django.shortcuts import render

# Create your views here.


# обязательно указывать request!!!
def index(request):
    context = {
        'page_title': 'главная'
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context = {
        'page_title': 'каталог',
    }

    return render(request, 'mainapp/catalog/catalog.html', context)


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
