from django.contrib.auth.models import User
from django.shortcuts import render
from task.models import Item, PurchaseList, PurchaseItems
from rest_framework.views import APIView
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


class GetGeneratedInvoiceView(APIView):
    def get(self, request, *args, **kwargs):
        purchase_id = self.kwargs.get("id")
        purchase_list = PurchaseList.objects.filter(id=purchase_id).first()
        import ipdb; ipdb.set_trace()