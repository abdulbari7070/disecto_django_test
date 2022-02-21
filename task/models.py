from django.db import models
from django.contrib.auth import get_user_model
# from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
    @property
    def in_stock(self):
        if self.in_stock_quantity > 0:
            return True
        return False 
       
    
class PurchaseList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # phone_number = models.PhoneNumberField(null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.username
    
    
class PurchaseItems(models.Model):
    order = models.ForeignKey(PurchaseList, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="item_list", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.item.name} - {self.order.user.username}"
    
    class Meta:
        verbose_name_plural = "Purchase Items"

     