from django.shortcuts import render
from task.models import Item
from rest_framework.generics import ListAPIView
from task.serializers import ItemSerializer


class GetAvailableProductList(ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(in_stock_quantity__gt=0)
    