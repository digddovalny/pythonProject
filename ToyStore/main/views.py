from django.http import HttpResponse
from django.shortcuts import render

from products.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин игрушек ToyVip',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать в мир волшебства и веселья - добро пожаловать в мой интернет-магазин ToyVip! '
                        'Данный интернет-магазин был выбран в качестве дипломного проекта GeekBrains. '
                        'Спасибо, что посетили сайт магазина ToyVip.'
    }
    return render(request, 'main/about.html', context)
