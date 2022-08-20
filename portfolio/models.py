from django.db import models

# Create your models here.

#Esta clase representará una tabla dentro de la base de datos. 
#Lo hacemos heredando de la clase Model

#agregamos los atributos con el tipo de datos de Models
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") #agregamos el campo verbose para describir
    description =  models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)#el atributo upload_to, permite idnicar donde subir las imagenes
    link = models.URLField(null=True, blank=True, verbose_name="Enlace Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta: #creamos una subclase con Meta información:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente
    
    def __str__(self): # redefinimosel método especial __str__ para que devuelva la cadena que nosotros queramo
        return self.title

        
        
