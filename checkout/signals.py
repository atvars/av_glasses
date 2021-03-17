from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def edit_on_save(sender, instance, created, **kwargs):
    """
    Edit and save order total on lineitem update/create
    """
    instance.order.edit_total()


@receiver(post_delete, sender=OrderLineItem)
def edit_on_save(sender, instance, **kwargs):
    """
    Edit and save order total on lineitem delete
    """
    instance.order.edit_total()
