from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_successful/<order_code>', views.payment_successful, name='payment_successful'),
    path('checkout_data/', views.checkout_data, name='checkout_data'),
    path('swh/', webhook, name='webhook'),
]
