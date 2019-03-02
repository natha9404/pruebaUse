from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
from rest_framework import permissions
from .models import Tablero, Tarjeta
from usuarios.models import Usuario
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from datetime import datetime
import pytz





Resp = Response_Builder()

# Create your views here.


class CrearTablero(APIView):

    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    @api_view(['GET'])
    def dispatch(self, request, *args, **kwargs):
        return super(CrearTablero, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        jsonTablero = request.data['crearTablero']

        try:
            nombreTablero = jsonTablero['nombreTablero']
            estado = jsonTablero['estado']

            username = request.user.username
            usuario = Usuario.objects.get(username=username)
            propietario = usuario

            tablero = Tablero()
            tablero.nombreTablero = nombreTablero
            tablero.estado = estado
            tablero.propietario = propietario
            tablero.save()

            return Resp.send_response(_status=200, _msg='OK', _data='Tablero creado exitosamente')
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='El tablero no pudo ser creado')


class CrearTarjeta(APIView):

    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    @api_view(['GET'])
    def dispatch(self, request, *args, **kwargs):
        return super(CrearTablero, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        jsonTarjeta = request.data['CrearTarjeta']

        try:
            now_utc = datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0)
            titulo = jsonTarjeta['titulo']
            idTablero = jsonTarjeta['idTablero']
            contenido = jsonTarjeta['contenido']
            ultimaModificacion = now_utc.strftime("%Y-%m-%d %H:%M:%S")

            username = request.user.username

            # If para comprobar si el tablero al que se le añadira la tarjeta pertenece al usuario logueado
            tablero = Tablero.objects.get(id=idTablero)
            usuario = Usuario.objects.get(username=username)

            if tablero.propietario.username == usuario.username:
                propietario = usuario

                tarjeta = Tarjeta()
                tarjeta.titulo = titulo
                tarjeta.idTablero = tablero
                tarjeta.contenido = contenido
                tarjeta.ultimaModificacion = ultimaModificacion
                tarjeta.save()
                return Resp.send_response(_status=200, _msg='OK', _data='Tarjeta creado exitosamente')
            else:
                return Resp.send_response(_status=503, _msg='Usted no posee permisos para añadir '
                                                            'tarjetas en este tablero')

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='La tarjeta no pudo ser creada')
