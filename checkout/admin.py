from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_code', 'date',
                       'delivery_price', 'total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_code', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_price',
              'total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_code', 'date', 'full_name',
                    'total', 'delivery_price',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
