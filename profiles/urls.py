from django.urls import path
from . import views
from newsletter.api import api_add_subscriber

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_code>', views.order_history, name='order_history'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),
]
