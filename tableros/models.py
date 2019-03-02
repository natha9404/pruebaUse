from django.db import models
from usuarios.models import Usuario

# Create your models here.

ESTADO_CHOICES = (('Privado', 'Privado'), ('Público', 'Público'))

class Tablero(models.Model):
    nombreTablero = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, verbose_name="estado", default='Privado', choices=ESTADO_CHOICES)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTablero


class Tarjeta(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    ultimaModificacion = models.DateTimeField(auto_now_add=False, default=False, editable=False)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class SolicitudAprobacion(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    nuevoTitulo = models.CharField(max_length=100)
    nuevoContenido = models.TextField()
    fechaModificacion = models.DateTimeField(auto_now_add=False, default=False, editable=False)
    usuarioSolicitud = models.ForeignKey(Usuario, on_delete=models.CASCADE)