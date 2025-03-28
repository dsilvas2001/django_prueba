from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la imagen")  # Ej: "gato.jpg"
    tipo_detectado = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tipo detectado")  # Lo llenará Lambda
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")  # Lo llenará Lambda
    archivo = models.ImageField(upload_to="imagenes/", verbose_name="Archivo de imagen")  # Se guarda en /media/imagenes/

    def __str__(self):
        return self.nombre  # Muestra el nombre en el panel de administración

    class Meta:
        verbose_name = "Imagen"  # Nombre singular en el admin
        verbose_name_plural = "Imágenes"  # Nombre plural