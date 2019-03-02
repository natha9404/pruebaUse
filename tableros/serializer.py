from rest_framework import serializers
from .models import *
from usuarios.serializer import UsuarioSerializer

class TableroSerializerPublico(serializers.ModelSerializer):
    propietario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Tablero
        fields = '__all__'


class TableroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tablero
        fields = '__all__'


class TarjetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarjeta
        fields = '__all__'