from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario (User):
    segundo_nombre = models.CharField(max_length=100, verbose_name="Segundo Nombre", blank=True, validators=[alpha])
    segundo_apellido = models.CharField(max_length=100, verbose_name="Segundo Apellido", blank=True, validators=[alpha])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
