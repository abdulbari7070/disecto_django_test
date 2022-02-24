from django.urls import path
from task.views import GetAvailableProductListView, CreateOrderView, GetGeneratedInvoiceView, geeks_view


urlpatterns = [
    path('get_products', GetAvailableProductListView.as_view(), name="get_products"),
    path('create_order', CreateOrderView.as_view(), name="create_order"),
    path('get_invoice/<int:id>', GetGeneratedInvoiceView.as_view(), name="get_generated_invoice"),
    path('geeks_view/', geeks_view),
]
