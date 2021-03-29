from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Render user profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully')

        else:
            messages.error(request, 'Update failed. Please check your form and try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_code):
    order = get_object_or_404(Order, order_code=order_code)

    messages.info(request, (
        f'This is a confirmation for order number {order_code}. '
        'Confirmation email was sent to you.'
    ))

    template = 'checkout/payment_successful.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
