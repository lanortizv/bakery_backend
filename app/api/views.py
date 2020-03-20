from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PersonList(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class Order_productsList(generics.ListCreateAPIView):
    queryset=Order_products.objects.all()
    serializer_class=Order_productsSerializer

class Order_productsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order_products.objects.all()
    serializer_class=Order_productsSerializer