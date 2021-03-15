from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_cart(request):
    """ A view that shows the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'You changed {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'You aded {product.name} to your shoping cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'You changed {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'You deleted {product.name} from your shoping cart')


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """Delete the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)
            messages.success(request, f'You deleted {product.name} from your shoping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
