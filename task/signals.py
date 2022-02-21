from django.db.models.signals import post_save
from task.models import PurchaseItems
from django.dispatch import receiver


@receiver(post_save, sender=PurchaseItems)
def update_quantity(sender, instance, created, **kwargs):
    if created:
        stock = instance.item.in_stock_quantity
        order_quantity = instance.quantity
        new_stock = stock - order_quantity
        instance.item.in_stock_quantity = new_stock
        instance.item.save()