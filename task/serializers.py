from rest_framework.serializers import ModelSerializer
from task.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"