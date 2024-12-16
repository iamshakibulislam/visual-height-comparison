from django.shortcuts import render
from .models import blogpost

# Create your views here.
def blog_(request,slug):

	post = blogpost.objects.get(url = slug)




	return render(request,"blogpost.html",{"post":post})