from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import *
from datetime import datetime, timedelta
from django.conf import settings
import stripe



stripe.api_key = settings.STRIPE_SECRET_KEY

class Homepage(View):
	template_name = 'index.html'
	def get(self,request):
		return render(request, self.template_name, context)


class SignUp(View):
	template_name = 'sign-up.html'
	def get(self,request):
		return render(request, self.template_name, {})
	def post(self,request):
		try:
			name  = request.POST.get("name")
			print(name)
			email  = request.POST.get("email")
			print(email)
			password= request.POST.get("pass")
			print(password)
			retypepassword  = request.POST.get("re_pass")
			print(retypepassword)
			phonenumber = request.POST.get("phonenumber")
			print(phonenumber)
			customer = Customer.objects.create(name=name,email=email,
				password=password,retypepassword=retypepassword,phonenumber=phonenumber)
			print(customer)
		except Exception as e:
			raise e 
		return HttpResponseRedirect('/')

class Login(View):
	template_name = 'login.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,{})
	def post(self, request):
		username = request.POST.get("username")
		print(username)
		password = request.POST.get("passwords")
		print(password)
		try:
			user = Customer.objects.get(name=username)
			userauth = authenticate(username=user, password=password)
			if userauth:
				login(request, user)
		except Exception as e:
			raise e 
		return HttpResponseRedirect('/')

class Product(View):
	template_name = 'product-one.html'
	def get(self,request):
		product = Products.objects.all()
		products = Products.objects.get(id=1)
		print(product)
		start = datetime.now().date()
		print(start)
		end = products.enddate
		print(end)
		diff =  end - start 
		print(diff)
		amount = products.minimum_deposit
		print(amount)
		context = {
		'product': product,
		'diff':diff.days,
		'amount':amount


		}
		context['key'] = settings.STRIPE_PUBLISHABLE_KEY
		return render(request,self.template_name, context)
	def post(self,request):
		pid = request.POST.get('productid')
		
		products = Products.objects.get(id=pid)
		order,created = Order.objects.get_or_create(product_id=products)
		print(order)
		orders_id = order.order_id
		print(orders_id)
		amount = products.minimum_deposit
		charge = stripe.Charge.create(
			amount=amount,
			currency='usd',
			description='A Django charge',
			source=request.POST['stripeToken'],
			metadata={'order_id':orders_id }
			)
		status = charge.paid
		if status==True:
			order.order_status=1
			order.payment_status = 1
			
		else:
			print("payment failed ")

		order.save()
		return HttpResponseRedirect('/')


