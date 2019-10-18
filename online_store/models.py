# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Retailer(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=500)


class User(models.Model):
    user_name = models.CharField(null=False, max_length=50)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    

class Category(models.Model):
    name = models.CharField(null=False, max_length=50)
    

class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
    category = models.ManyToManyField(Category)
    stock_quantity = models.IntegerField()


class Order(models.Model):
    fulfilled = models.BooleanField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    
class Review(models.Model):
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)