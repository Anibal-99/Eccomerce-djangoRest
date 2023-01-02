from apps.base.api import GeneralListApiView
from apps.products.api.serializers.products_serializers import ProductsSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class ProductsListApiViews(GeneralListApiView):
    serializer_class=ProductsSerializer

class ProductCreateApiView(generics.CreateAPIView):
    serializer_class=ProductsSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class=ProductsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class ProductDestroyApiView(generics.DestroyAPIView):
    serializer_class=ProductsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def delete(self, request, pk=None):
        product=self.get_queryset().filter(id=pk).first()
        if product:
            product.state=False
            product.save()
            return Response({'message':'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
