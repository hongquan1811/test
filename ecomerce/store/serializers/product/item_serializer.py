from rest_framework import  serializers
from ...models.product.item import Item
from .product_serializer import ProductSerializer

class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Item
        fields = '__all__'
        depth = 1