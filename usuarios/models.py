from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Unicamente se aceptan caracteres alfanumericos.')
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Unicamente se aceptan caracteres alfanumericos.')
numeric = RegexValidator(r'^[0-9]*$', 'Solamente valores númericos')


def get_upload_to(instance, filename):
    return 'upload/%s/%s' % (instance.numero_documento_identificacion, filename)

# Create your models here.
class Usuario (User):
    Token_validity_duration = timedelta(days=7)
    segundo_nombre = models.CharField(max_length=100, verbose_name="Segundo Nombre", blank=True, validators=[alpha])
    segundo_apellido = models.CharField(max_length=100, verbose_name="Segundo Apellido", blank=True, validators=[alpha])
    numero_documento_identificacion = models.CharField(max_length=20,
                                                       verbose_name="Número de documento de identificación",
                                                       validators=[numeric])
    foto = models.ImageField(upload_to=get_upload_to, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
