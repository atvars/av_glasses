from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_client_secret = settings.STRIPE_CLIENT_SECRET
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Shoping Cart Is Empty")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_client_secret
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_publishable_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_publishable_key': 'pk_test_51IVvlOEglCmSP1bOJzK2YX2F2Io1fpEvUnrVqB3v2cbXez8T3B6yoy4r0Y5zntUXA3JOSMRs8hLoSrFtdwzuzPk800WSNP11V3',
        'stripe_client_secret': 'test client key',
    }

    return render(request, template, context)
