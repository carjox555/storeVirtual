from django.contrib import admin

# Register your models here. registramos nuestra app
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio,ServicioAdmin)