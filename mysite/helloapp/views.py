from django.shortcuts import render
from django.http import HttpResponse

def hello(request,name):
    # name = request.GET['name']
    return HttpResponse("Hello {}".format(name))

def calc(request, a, b):
    return HttpResponse("{}+{}={}".format(a,b, (a+b)))
