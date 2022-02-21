from django.urls import path
from task.views import GetAvailableProductList


urlpatterns = [
    path('get_products', GetAvailableProductList.as_view(),name="get_products"),
]
