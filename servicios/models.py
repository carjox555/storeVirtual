from email.headerregistry import ContentDispositionHeader
from pyexpat import model
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField()
    created=models.DateTimeField(auto_now_add=True) #fecha en la que se creo un servicio
    update=models.DateTimeField(auto_now_add=True) #fecha en la que se modifica

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    #funcion 
    def __str__(self):
        return self.titulo