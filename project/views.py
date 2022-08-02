from urllib import response
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


#class UserViewSet(viewsets.ModelViewSet):
  #  """
   # API endpoint that allows users to be viewed or edited.
    #"""
  # # queryset = User.objects.all().order_by('-date_joined')
  # # serializer_class = UserSerializer
  # # permission_classes = [permissions.IsAuthenticated]

#
#class GroupViewSet(viewsets.ModelViewSet):
   # """
   # API endpoint that allows groups to be viewed or edited.
  #  """
  # # queryset = Group.objects.all()
  # # serializer_class = GroupSerializer
  # # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def apiOverView(request):
    api_urls={
        'list': '/product_list/', #copy and paste '/product_list' on the url bar to see product list
        'detail view': '/product_detail/<int:id>',  #copy and paste '/product_detail/<int:id>' on the url bar to see to see detail view
        'create':'/product_create/',  #copy and paste '/product_create' on the url bar to see to create products
        'update':'/product_update/<int:id>/', #/copy and paste '/product_update/<int:id>/' on the url bar to update the product u wish
        'delete': '/product_delete/<int:id>/' #copy and paste '/product_delete/<int:id>' on the url bar to delte a product you wish.

    } 

    return Response(api_urls);



@api_view(['GET'])
def showProducts(request):
    products = Product.objects.all()
    serializer = ProductSerilizer(products, many=True)

    return Response(serializer.data)




@api_view(['GET'])
def productDetail(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerilizer(product, many=False)

    return Response(serializer.data)



@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerilizer(data =request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)   




@api_view(['POST'])
def productUpdate(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerilizer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Item deleted successfully!")




