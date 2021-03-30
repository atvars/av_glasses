from django.urls import path
from . import views
from .webhooks import webhook
from newsletter.api import api_add_subscriber

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_successful/<order_code>', views.payment_successful, name='payment_successful'),
    path('checkout_data/', views.checkout_data, name='checkout_data'),
    path('swh/', webhook, name='webhook'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

]
