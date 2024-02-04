from django.shortcuts import render, get_list_or_404, get_object_or_404

from products.models import Products


def catalog(request, category_slug):
    if category_slug == 'All':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        'title': 'Home - Каталог',
        'products': products,
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)
