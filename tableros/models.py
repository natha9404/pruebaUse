from django.db import models
from users.models import Usuario

# Create your models here.

ESTADO_CHOICES = (('Privado', 'Privado'), ('Público', 'Público'))

class Tablero(models.Model):
    nombreTablero = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, verbose_name="estado", default='Privado', choices=ESTADO_CHOICES)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTablero


class Card(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    contenido = models.TextField()
    ultimaModificacion = models.DateTimeField(auto_now_add=False, default=False, editable=False)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo