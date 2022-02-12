from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Blog Index working')

def temp(request):
	return render(request, 'blog/blog.html')