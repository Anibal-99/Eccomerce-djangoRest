from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductsSerializer, IndicatorSerializer

class MeasureUnitListApiView(GeneralListApiView): # clase generica que tiene drf para listar
    serializer_class = MeasureUnitSerializer

class CategoryProductListApiView(GeneralListApiView): # clase generica que tiene drf para listar
    serializer_class = CategoryProductsSerializer

class IndicatorListApiView(GeneralListApiView): # clase generica que tiene drf para listar
    serializer_class = IndicatorSerializer
