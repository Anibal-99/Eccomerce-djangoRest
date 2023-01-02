from apps.products.models import Products
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductsSerializer, IndicatorSerializer

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Products
        exclude=('state','created_date', 'modified_date', 'deleted_date',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description':instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product':instance.category_product.description,
        }
