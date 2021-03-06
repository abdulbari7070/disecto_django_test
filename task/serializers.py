from rest_framework.serializers import ModelSerializer, ValidationError
from task.models import Item, PurchaseList, PurchaseItems
from django.db import transaction


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PurchaseItemSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItems
        fields = ('order', 'item', 'quantity')
        read_only_fields = ('order',)


class PurchaseListSerializer(ModelSerializer):
    item_list = PurchaseItemSerializer(many=True, write_only=True)

    class Meta:
        model = PurchaseList
        fields = ('user', 'order_date', 'is_paid', 'address', 'city', 'state', 'zipcode', 'item_list')
        
    def validate(self, data):
        """
        Check the quantity in stock for purchased item
        """
        item_list = data["item_list"]
        for item in item_list:
            if item["quantity"] > item["item"].in_stock_quantity:
                item_name = item["item"].name
                item_in_stock = item["item"].in_stock_quantity
                raise ValidationError({
                "general_errors": [
                    f"Stock available for {item_name} is {item_in_stock}"
                ]
            })
        return data

    @transaction.atomic()
    def create(self, validated_data):
        """
        Create Purchase List object and pass it in Purchase items to create Purchase Items
        """
        purchase_item_data = validated_data.pop("item_list")
        order = PurchaseList.objects.create(**validated_data)
        for each_item in purchase_item_data:
            item = PurchaseItems.objects.create(order=order, **each_item)
        return order

    # @transaction.atomic()
    # def create(self, validated_data):
    #     purchase_item_data = validated_data.pop("item_list")
    #     order = PurchaseList.objects.create(**validated_data)
    #     for each_item in purchase_item_data:
    #         # each_item["item"] = each_item["item"].id
    #         # purchase_item = PurchaseItems(order=order)
    #         # PurchaseItems.objects.create(order=order, **each_item)
    #         # import ipdb; ipdb.set_trace()
    #         item_list_serializer = PurchaseItemSerializer(order=order, **each_item)

    #         # item_list_serializer = PurchaseItemSerializer(purchase_item, **each_item)
    #         if item_list_serializer.is_valid():
    #             item_list_serializer.save()
    #         # else:
    #         #     raise ValidationError(item_list_serializer.errors)
    #     return order

