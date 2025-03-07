from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
import os

def index(request):
    template = loader.get_template("item/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def product(request):
    template = loader.get_template("item/product.html")
    context = {}
    return HttpResponse(template.render(context, request))

def cart(request):
    template = loader.get_template("item/cart.html")
    context = {}
    return HttpResponse(template.render(context, request))
