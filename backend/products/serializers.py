from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from products.validators import validate_title_no_hello,unique_product_title
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
     url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
     )
     title = serializers.CharField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all',
    #     read_only=True,many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='product-detail',
    #     lookup_field='pk',
    # )
    # title = serializers.CharField(validators = [validate_title])
    title = serializers.CharField(validators = [validate_title_no_hello,unique_product_title])
    # email = serializers.EmailField(source='user.email',read_only=True)
    # name = serializers.CharField(source='title',read_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',#user_id
            # 'url',
            # 'edit_url',
            # 'email',
            'pk',
            # 'name',
            'title',
            # 'content',
            'body',
            'price',
            'sale_price',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products',
            'public',
            'path',
            'endpoint',
        ]
    def get_my_user_data(self,obj):
        return {
            "username":obj.user.username
        }


    # def validate_title(self,value):
    #     request = self.context.get('request')
    #     user = request.user
    
    #     qs = Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already product name")
        
    #     return value 


    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     # instance.title = validated_data.get('title')
    #     # return instance
    #     return super().update(instance,validated_data)


    # def get_url(self,obj):
    #     # return f"/api/products/{obj.pk}/"
    #     request = self.context.get('request')#self.request
    #     if request is None:
    #         return None
    #     return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_edit_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')#self.request
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    

    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        # print(obj.id)
        #obj.user -> user.username
        #obj.category ->
        return obj.get_discount()
    