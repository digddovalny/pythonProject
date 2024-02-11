from django.db import transaction
from django.shortcuts import render
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

from orders.forms import CreateOrderForm

from baskets.models import Basket

from orders.models import Order

from orders.models import OrderItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Basket.objects.filter(user=user)

                    if basket_items.exists():

                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for basket_item in basket_items:
                            product = basket_item.product
                            name = basket_item.product.name
                            price = basket_item.product.selling_price()
                            quantity = basket_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно количества товара {name} на складе.'
                                                      f' Всего в наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        basket_item.delete()

                        messages.success(request, 'Заказ оформлен')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('basket:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформление заказа',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)
