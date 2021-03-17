import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_code = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_code(self):
        """
        Create unique order code using UUID
        """
        return uuid.uuid4().hex.upper()

    def edit_total(self):
        """
        Edit total each time a line item is added,
        accounting for delivery price.
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.total < settings.FREE_DELIVERY_POINT:
            self.delivery_price = self.total * settings.STANDARD_DELIVERY / 100
        else:
            self.delivery_price = 0
        self.grand_total = self.total + self.delivery_price
        self.save()

    def save(self, *args, **kwargs):
        """
        Change original save method to set the order code
        if it hasn't been set already.
        """
        if not self.order_code:
            self.order_code = self._create_order_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_code


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Change original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'name {self.product.name} on order {self.order.order_code}'
