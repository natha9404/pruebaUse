from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
from rest_framework import permissions, authentication
from .models import Tablero, Tarjeta
from usuarios.models import Usuario
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .serializer import *
import pytz


Resp = Response_Builder()

# Create your views here.


class CrearTablero(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

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
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def post(self, request, format=None):
        jsonTarjeta = request.data['crearTarjeta']

        try:
            now_utc = datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0)
            titulo = jsonTarjeta['titulo']
            idTablero = jsonTarjeta['idTablero']
            contenido = jsonTarjeta['contenido']
            ultimaModificacion = now_utc.strftime("%Y-%m-%d %H:%M:%S")

            username = request.user.username

            # If para comprobar si el tablero al que se le añadira la tarjeta pertenece al usuario logueado
            try:
                print(idTablero)
                tablero = Tablero.objects.get(id=idTablero)
                print(tablero)
                usuario = Usuario.objects.get(username=username)
            except:
                return Resp.send_response(_status=503, _msg='El tablero no existe')


            if tablero.propietario.username == usuario.username:
                propietario = usuario

                tarjeta = Tarjeta()
                tarjeta.titulo = titulo
                tarjeta.tablero = tablero
                tarjeta.contenido = contenido
                tarjeta.ultimaModificacion = ultimaModificacion
                tarjeta.save()
            else:
                return Resp.send_response(_status=503, _msg='Usted no posee permisos para añadir '
                                                            'tarjetas en este tablero')

            return Resp.send_response(_status=200, _msg='OK', _data='Tarjeta creado exitosamente')
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='La tarjeta no pudo ser creada')


class ListarTablerosUsuario(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def get(self, request, format=None):
        try:
            username = request.user.username
            tableros = Tablero.objects.filter(propietario__username=username)
            serializer = TableroSerializer(tableros, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serializer.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar los tableros')


class ListarTablerosPublicos(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def get(self, request, format=None):
        try:
            tableros = Tablero.objects.filter(estado='Público')
            serializer = TableroSerializerPublico(tableros, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serializer.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar los tableros')


class ListarTarjetasTablero(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def post(self, request, format=None):
        print(2, request.META.get('HTTP_AUTHORIZATION'))

        try:
            jsonTablero = request.data['listarTarjetas']
            idTablero = jsonTablero['idTablero']
            tablero = Tablero.objects.get(id=idTablero)
            estadoTablero = tablero.estado
            propietario = tablero.propietario.username
            usuarioLogueado = request.user.username

            if estadoTablero =='Público':
                tarjetas = Tarjeta.objects.filter(tablero_id=idTablero)
            else:
                if usuarioLogueado == propietario:
                    tarjetas = Tarjeta.objects.filter(tablero_id=idTablero)
                else:
                    return Resp.send_response(_status=503, _msg='El tablero no es público')

            print(tarjetas)

            serializer = TarjetaSerializer(tarjetas, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serializer.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar las tarjetas')