from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main.html")



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
