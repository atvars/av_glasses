from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_successful/<order_code>', views.payment_successful, name='payment_successful'),
]
