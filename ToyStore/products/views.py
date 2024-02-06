from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404

from products.models import Products

from products.utils import query_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    with_sale = request.GET.get('with_sale', None)
    orderb = request.GET.get('orderb', None)
    query = request.GET.get('q', None)

    if category_slug == 'All':
        products = Products.objects.all()
    elif query:
        products = query_search(query)
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if with_sale:
        products = products.filter(discount__gt=0)
    if orderb and orderb != 'default':
        products = products.order_by(orderb)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'products': current_page,
        'slug_url': category_slug
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)
