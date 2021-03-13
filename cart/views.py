from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ A view that shows shoping bag contents page """

    return render(request, 'cart/cart.html')
