from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('people/',PersonList.as_view()),
    path('person/<int:pk>',PersonDetail.as_view()),
    path('orders/',OrderList.as_view()),
    path('order/<int:pk>',OrderDetail.as_view()),
    path('products/',ProductList.as_view()),
    path('product/<int:pk>',PersonList.as_view()),
    path('orderProducts/',Order_productsList.as_view()),
    path('orderProduct/<int:pk>',Order_productsDetail.as_view()),
]
