from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request, "main.html", {'product': product})