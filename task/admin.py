from django.contrib import admin
from task.models import Item, PurchaseList, PurchaseItems


admin.site.register(Item)
admin.site.register(PurchaseList)
admin.site.register(PurchaseItems)
