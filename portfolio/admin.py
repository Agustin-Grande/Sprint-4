from django.contrib import admin

#importamos el modelo Project definido en el archivo Model
from .models import Project

# Register your models here.

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')

#Con esta instruccion registramos Project para que pueda ser gestionado en el admin
admin.site.register(Project)