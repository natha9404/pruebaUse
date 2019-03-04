from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
from rest_framework import permissions, authentication
from .models import Tablero, Tarjeta, SolicitudAprobacion
from usuarios.models import Usuario
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .serializer import *
import pytz
import json


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
                tablero = Tablero.objects.get(id=idTablero)
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

            jsonFinal = {}

            for index, tablero in enumerate(tableros, start=0):
                tarjetas = Tarjeta.objects.filter(tablero=tablero)
                tarjetasSerializada = TarjetaSerializer(tarjetas, many=True)

                jsonTemporal = {
                    "idTablero": tablero.id,
                    "nombreTablero": tablero.nombreTablero,
                    "tarjetas" : tarjetasSerializada.data

                }


                jsonFinal[index] = jsonTemporal


            return Resp.send_response(_status=200, _msg='OK', _data=jsonFinal)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar los tableros')


class ListarTablerosPublicos(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def get(self, request, format=None):
        try:
            tableros = Tablero.objects.filter(estado='Público')
            jsonFinal = {}

            for index, tablero in enumerate(tableros, start=0):
                tarjetas = Tarjeta.objects.filter(tablero=tablero)
                tarjetasSerializada = TarjetaSerializer(tarjetas, many=True)

                jsonTemporal = {
                    "idTablero": tablero.id,
                    "nombreTablero": tablero.nombreTablero,
                    "tarjetas": tarjetasSerializada.data

                }

                jsonFinal[index] = jsonTemporal

            return Resp.send_response(_status=200, _msg='OK', _data=jsonFinal)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar los tableros')


class ListarTarjetasTablero(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def post(self, request, format=None):

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

            serializer = TarjetaSerializer(tarjetas, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serializer.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se pueden listar las tarjetas')


class ActualizarTarjeta(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def post(self, request, format=None):

        try:
            now_utc = datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0)
            print(request.data)
            usuarioLogueado = request.user.username

            idTarjeta = request.data['idTarjeta']
            contenido = request.data['contenido']
            ultimaModificacion = now_utc.strftime("%Y-%m-%d %H:%M:%S")

            try:
                tarjeta = Tarjeta.objects.get(id=idTarjeta)
            except:
                return Resp.send_response(_status=503, _msg='La tarjeta no existe')


            estadoTablero = tarjeta.tablero.estado
            propietario = tarjeta.tablero.propietario.username

            if(propietario==usuarioLogueado):
                tarjeta.contenido = contenido
                tarjeta.ultimaModificacion = ultimaModificacion
                tarjeta.save()
                return Resp.send_response(_status=200, _msg='Tarjeta actualizada correctamente')

            else:
                if(estadoTablero=='Público'):
                    try:
                        usuarioLog = Usuario.objects.get(username=usuarioLogueado)
                    except:
                        return Resp.send_response(_status=503, _msg='El usuario no existe')

                    solicitud = SolicitudAprobacion()
                    solicitud.tarjeta = tarjeta
                    solicitud.fechaModificacion = ultimaModificacion
                    solicitud.nuevoContenido = contenido
                    solicitud.nuevoTitulo = tarjeta.titulo
                    solicitud.usuarioSolicitud = usuarioLog
                    solicitud.save()
                    return Resp.send_response(_status=200, _msg='Solicitud realizada exitosamente')

                else:
                    return Resp.send_response(_status=503, _msg='No tiene permisos para editar esta tarjeta')
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se puede actualizar la tarjeta')


class AceptarSolicitud(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def post(self, request, format=None):

        try:
            now_utc = datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0)
            idSolicitud = request.data['solicitud']

            usuarioLogueado = request.user.username

            solicitud = SolicitudAprobacion.objects.get(id=idSolicitud)
            solicitud.estado = 'Aprobada'
            solicitud.save()

            idTarjeta = solicitud.tarjeta.id

            titulo = solicitud.nuevoTitulo
            contenido = solicitud.nuevoContenido


            ultimaModificacion = now_utc.strftime("%Y-%m-%d %H:%M:%S")

            try:
                tarjeta = Tarjeta.objects.get(id=idTarjeta)
                propietario = tarjeta.tablero.propietario.username

                if usuarioLogueado == propietario:
                    tarjeta.titulo = titulo
                    tarjeta.contenido = contenido
                    tarjeta.ultimaModificacion = ultimaModificacion
                    tarjeta.save()
                return Resp.send_response(_status=200, _msg='Solicitud aceptada')


            except Exception as e:
                print(e)
                return Resp.send_response(_status=503, _msg='La tarjeta no existe')

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se puede actualizar la tarjeta')


class ListarSolicitudes(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def get(self, request, format=None):

        try:
            now_utc = datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0)
            usuarioLogueado = request.user.username
            usuario = Usuario.objects.get(username=usuarioLogueado)

            solicitudes = SolicitudAprobacion.objects.filter(tarjeta__tablero__propietario=usuario)
            serializado = SolicitudSerializer(solicitudes, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serializado.data)

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='No se puede listar las solicitudes')

