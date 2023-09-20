from django.urls import path
# from products.views import ProductDetailAPIView
from products.views import product_detail_view,product_list_create_view
from products.views import product_alt_view
from products.views import product_update_view
from products.views import product_delete_view
from products.views import product_mixin_view

urlpatterns = [
    path('',product_list_create_view,name='product-list'),
    # path('',product_mixin_view),
    path('<int:pk>/update/',product_update_view,name='product-edit'),
    path('<int:pk>/delete/',product_delete_view),
    path('<int:pk>/',product_detail_view,name='product-detail'),
    # path('<int:pk>/',product_mixin_view),
]