from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListApiView, CategoryProductListApiView, IndicatorListApiView
from apps.products.api.views.products_views import ProductsListApiViews, ProductCreateApiView, ProductRetrieveApiView, ProductDestroyApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListApiView.as_view(), name='measure_unit'),
    path('category_products/', CategoryProductListApiView.as_view(), name='category_products'),
    path('indicator/', IndicatorListApiView.as_view(), name='indicator'),
    path('products/list/', ProductsListApiViews.as_view(), name='list_products'),
    path('products/create/', ProductCreateApiView.as_view(), name='create_products'),
    path('products/retrieve/<int:pk>', ProductRetrieveApiView.as_view(), name= 'retrieve_products'),
    path('products/destroy/<int:pk>', ProductDestroyApiView.as_view(), name= 'destroy_products'),
]
