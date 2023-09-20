# from api.authentication import TokenAuthentication
# from django.http import Http404
from requests import Response
from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin
from api.mixins import UserQuerySetMixin
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self,serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         None
#         if content is None:
#             content = title
#         serializer.save(content=content)

# product_create_view = ProductCreateAPIView.as_view()

# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # authentication_classes = [
#     #     authentication.SessionAuthentication,
#     #     # authentication.TokenAuthentication
#     #     TokenAuthentication
#     #     ] ---->used in setting
#     permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

#     def perform_create(self,serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         None
#         if content is None:
#             content = title
#         serializer.save(content=content)

# product_list_create_view = ProductListCreateAPIView.as_view()


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # allow_staff_view =False


    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication
    #     TokenAuthentication
    #     ] ---->used in setting

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.pop('email')
        # print(email)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user,content=content)

    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(request.user)
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

#     #lookup_field ='pk' ??
    
# product_detail_view = ProductDetailAPIView.as_view()

class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #lookup_field ='pk' ??
    
product_detail_view = ProductDetailAPIView.as_view()


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.DjangoModelPermissions]
#     lookup_field ='pk'
#     permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]


#     def perform_update(self,serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content - instance.title
    
# product_update_view = ProductUpdateAPIView.as_view()

class ProductUpdateAPIView(
    UserQuerySetMixin,
     StaffEditorPermissionMixin,
     generics.UpdateAPIView
     ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'
    
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content - instance.title
    
product_update_view = ProductUpdateAPIView.as_view()


# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field ='pk'
#     permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]


#     def perform_destroy(self,instance):
#         super().perform_destroy(instance)
    
# product_delete_view = ProductDestroyAPIView.as_view()


class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'
    
    def perform_destroy(self,instance):
        super().perform_destroy(instance)
    
product_delete_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):

#     '''
#     Not using this
#     '''

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# produt_list_view = ProductListAPIView.as_view()


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


product_mixin_view = ProductMixinView.as_view()




@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            #detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            obj = get_object_or_404(Product,pk=pk)
            print(obj)
            # data = ProductSerializer(obj,many=False).data
            data = ProductSerializer(obj, many=False).data
            print(data)
            return Response(data)
        #url_args??
        #get request -> detail view
        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)