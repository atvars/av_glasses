from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Shoping Cart Is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_publishable_key': 'pk_test_51IVvlOEglCmSP1bOJzK2YX2F2Io1fpEvUnrVqB3v2cbXez8T3B6yoy4r0Y5zntUXA3JOSMRs8hLoSrFtdwzuzPk800WSNP11V3',
        'stripe_client_secret': 'test client key',
    }

    return render(request, template, context)
