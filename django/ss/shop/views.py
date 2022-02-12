from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product

# Create your views here.


def index(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	nslide = n//4 + ceil((n/4)-(n//4))
	para = { 'no_of_slides':nslide , 'range':range(nslide) , 'product': products}
	return render(request,"home.html ")

def temp(request):
	return render(request, "shop.html")

def about(request):
	return render(request, "about.html")

def contact(request):
	return HttpResponse("contact is hear")

def view(request):
	return HttpResponse("product view is hear")

def out(request):
	return HttpResponse("checkout is hear")