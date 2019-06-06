from django.db import models
from datetime import datetime, timedelta
import uuid


class Customer(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	email = models.CharField(max_length=100,null=True,blank=True)
	password = models.CharField(max_length=100,null=True,blank=True)
	retypepassword = models.CharField(max_length=100,null=True,blank=True)
	phonenumber = models.CharField(max_length=12,null=True,blank=True)


	def __str__(self):
		return self.name

class Products(models.Model):
	title = models.CharField(max_length=100,null=True,blank=True)
	minimum_deposit =  models.IntegerField(null=True,blank=True)
	price = models.IntegerField(null=True,blank=True)
	main_image = models.ImageField(null=True,blank=True)
	product_image1  = models.ImageField(null=True,blank=True)
	product_image2 = models.ImageField(null=True,blank=True)
	product_image3 = models.ImageField(null=True,blank=True)
	created =  models.DateTimeField(auto_now_add=True,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	fullfilled_by = models.CharField(max_length=100,null=True,blank=True)
	enddate = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.title


class Bragets(models.Model):
	product_model = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
	bragets  = models.CharField(max_length=100,null=True,blank=True)
	price = models.IntegerField(null=True,blank=True)

class Order(models.Model):
	order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	product_id = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
	order_status = models.BooleanField(default=False,null=True,blank=True)
	payment_status = models.BooleanField(default=False,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	update = models.DateTimeField(auto_now=True,null=True,blank=True)

