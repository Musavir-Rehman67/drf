# import json
# from django.http import JsonResponse

# def api_home(request, *args,**kwargs):
#     #request -> Httprequest ->Django
#     # print(dir(request))
#     #request.body
#     print(request.GET) #url query params
#     body = request.body #byte string of JSON data
#     data = {}
#     try:
#         data = json.loads(body) #strung of JSON data -> Python dict
#     except:
#         pass

#     print(data)
#     # data['headers'] = request.headers #request.META ->
#     # header ={"Content_Type","application/json"}
#     # request.headers = header
#     # print(request.headers)
#     data['params'] = dict(request.GET)
#     data['headers']=dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
#     # return JsonResponse({"message":"Hi this is your Django API "})

# import json
# from django.http import JsonResponse,HttpResponse
# #JsonResponse accepts a dictionary as an argument
# #HttpResponse supposed to accept to be a string
# from products.models import Product
# from django.forms.models import model_to_dict

# def api_home(request,*args,**kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         # data = model_to_dict(model_data)
#         data = model_to_dict(model_data,fields=['id','title','price'])
#         # print(data)
#         # json_data_str = json.dumps(data)

#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price

#         # model instance (model_data)
#         # turn a python dict
#         # return JSON to my client

#     return JsonResponse(data)
#     # return HttpResponse(json_data_str,headers = {"content-type":"application/json"})





from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# @api_view(["GET","POST"])
# def api_home(request,*args,**kwargs):

#     """
#     DRF API View
#     """
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         # data = model_to_dict(model_data)
#         data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
#     return Response(data)


# @api_view(["GET"])
# def api_home(request,*args,**kwargs):

#     """
#     DRF API View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data ={}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)




@api_view(["POST"])
def api_home(request,*args,**kwargs):

    """
    DRF API View
    """
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)


















