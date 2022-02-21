from django.urls import path
from task.views import GetAvailableProductListView, CreateOrderView


urlpatterns = [
    path('get_products', GetAvailableProductListView.as_view(), name="get_products"),
    path('create_order', CreateOrderView.as_view(), name="create_order"),
]
