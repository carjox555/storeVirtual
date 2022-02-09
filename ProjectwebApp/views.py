from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

# Create your views here.
def home (request):
    return render(request,"ProjectwebApp/home.html")


def tienda (request):
    return render(request,"ProjectwebApp/tienda.html")

def blog (request):
    return render(request,"ProjectwebApp/blog.html")

def contacto (request):
    return render(request,"ProjectwebApp/contacto.html")
