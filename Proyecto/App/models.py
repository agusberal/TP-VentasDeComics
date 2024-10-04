from django.db import models

# Create your models here.
class Comics(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Autor = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=30)
    Fecha_Publicacion = models.DateField()
    Portada = models.ImageField(upload_to="Portadas",null=True)
    Sinopsis = models.TextField(blank=True)
  

    def __str__(self):
        return self.Codigo
