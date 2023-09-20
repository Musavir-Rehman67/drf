from rest_framework import mixins,viewsets
from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list ->Queryset
    get -> retrieve ->Product instance Detail view
    post -> create -> New Instance
    put -> update
    patch -> Partial Update
    delete - > destroy
    '''
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default




class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    '''
    get -> list ->Queryset
    get -> retrieve ->Product instance Detail view
    '''
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default


# product_list_view = ProductGenericViewSet.as_view({'get':'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})