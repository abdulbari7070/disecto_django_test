from django.contrib.auth.models import User
from django.shortcuts import render
from task.models import Item, PurchaseList, PurchaseItems
from rest_framework.generics import ListAPIView, CreateAPIView
from task.serializers import ItemSerializer, PurchaseListSerializer, PurchaseItemSerializer
from rest_framework.serializers import ValidationError


class GetAvailableProductListView(ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(in_stock_quantity__gt=0)


class CreateOrderView(CreateAPIView):
    model = PurchaseList
    serializer_class = PurchaseListSerializer
