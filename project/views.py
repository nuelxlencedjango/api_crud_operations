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
        'list': '/product_list/',
        'detail view': '/product_detail/<int:id>',
        'create':'/product_create/',
        'update':'/product_update/<int:id>/',
        'delete': '/product_delete/<int:id>/'

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




    