from tkinter import CASCADE
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #fecha en la que se creo un servicio
    update=models.DateTimeField(auto_now_add=True) #fecha en la que se modifica

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    #funcion para devolver nombre
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog',null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #ESTABELCEMOS RELACION
    categorias=models.ManyToManyField(Categoria)    # rel many to many varios a varios (clase categoria)
    created=models.DateTimeField(auto_now_add=True) #fecha en la que se creo un servicio
    update=models.DateTimeField(auto_now_add=True) #fecha en la que se modifica

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    #funcion 
    def __str__(self):
        return self.titulo