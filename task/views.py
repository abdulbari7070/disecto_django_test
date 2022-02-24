from django.contrib.auth.models import User
from django.shortcuts import render
from task.models import Item, PurchaseList, PurchaseItems
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from task.serializers import ItemSerializer, PurchaseListSerializer, PurchaseItemSerializer
from rest_framework.serializers import ValidationError
import pdfkit
from django.http import HttpResponse
from django.template import loader




class GetAvailableProductListView(ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(in_stock_quantity__gt=0)


class CreateOrderView(CreateAPIView):
    model = PurchaseList
    serializer_class = PurchaseListSerializer


from django.shortcuts import render

# Create your views here.
def geeks_view(request):
	
	# render function takes argument - request
	# and return HTML as response
    purchase_list = PurchaseList.objects.filter(id=28).first()

    return render(request, "invoice.html", {"purchase_list": purchase_list, "invoice_id": str(purchase_list.id).zfill(10), "total_price": total_price})


class GetGeneratedInvoiceView(APIView):
    
    
    def get(self, request, *args, **kwargs):
        purchase_id = self.kwargs.get("id")
        purchase_list = PurchaseList.objects.get(id=purchase_id)
        total_price = 0
        for item in purchase_list.items.all():
            total_price += (item.item.price*item.quantity)
        html = loader.render_to_string('invoice.html', {"purchase_list": purchase_list, "invoice_id": str(purchase_list.id).zfill(10), "total_price": total_price})
        output= pdfkit.from_string(html, output_path=False)
        response = HttpResponse(content_type="application/pdf")
        response.write(output)
        return response