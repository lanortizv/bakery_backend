from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    photo=models.ImageField(upload_to='people')
    user=models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    photo=models.ImageField(upload_to='products')

class Order(models.Model):
    time=models.DateTimeField()
    client=models.ForeignKey(User,null=True ,on_delete=models.SET_NULL,related_name='client')
    employer=models.ForeignKey(User,null=True ,on_delete=models.SET_NULL,related_name='employer')
    rate=models.FloatField()
    description=models.TextField()
    bill_number=models.CharField(max_length=30)
    bill_name=models.CharField(max_length=30)
    status=models.CharField(max_length=10)
    products=models.ManyToManyField(Product,through='order_products')

class Order_products(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.FloatField()
    description=models.TextField()
    time_created=models.DateTimeField()
    time_delivered=models.DateTimeField()








