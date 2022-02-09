#aqui se registra nuestra aplicacion 
#importamos
from django.contrib import admin
from .models import Servicio

#esta clase es para q aparesca en la web la opcion de creada y actualizada
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Servicio, ServicioAdmin)