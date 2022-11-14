from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField( verbose_name="Descripcion")
    image = models.ImageField( verbose_name="Imagen", upload_to="project")
    link = models.URLField( null=True, verbose_name="Direccion web")
    Created = models.DateTimeField(auto_now_add=True,  verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,  verbose_name="Fecha de actualizado")

    class Meta:
        verbose_name= "proyectos"
        verbose_name_plural= "proyectos"
        ordering =["-Created"]
        

    def __str__(self): 
        return  self.title
