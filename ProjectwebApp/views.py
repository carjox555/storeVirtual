from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    return render(request,"ProjectwebApp/home.html")

def servicios (request):
    return render(request,"ProjectwebApp/servicios.html")

def tienda (request):
    return render(request,"ProjectwebApp/tienda.html")

def blog (request):
    return render(request,"ProjectwebApp/blog.html")

def contacto (request):
    return render(request,"ProjectwebApp/contacto.html")
