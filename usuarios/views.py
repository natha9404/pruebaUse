from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from util.ResponseBuilder import Response_Builder
from config.errorMessages import ErrorMsg
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions, authentication
import json
from .serializer import UsuarioSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)





Resp = Response_Builder()
ErrorMSG = ErrorMsg()

# Create your views here.

class login(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            print(request.data)
            username = request.data["username"]
            password = request.data["password"]
            if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},
                                status=HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},
                                status=HTTP_404_NOT_FOUND)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                            status=HTTP_200_OK)
        except Exception as e:
            print(3, 'Error, no se puede realizar login' + str(e))
            return Resp.send_response(_status=503, _msg=ErrorMSG.get_msg(5003), _data=e)


class createUser(APIView):

    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:

            email = request.data['email']

            if Usuario.objects.filter(email=email).count() > 0:
                return Resp.send_response(_status=503, _msg='El correo electronico ya se encuentra registrado')
            else:
                first_name = request.data['primer_nombre']
                first_lastname = request.data['primer_apellido']
                segundo_nombre = request.data['segundo_nombre']
                segundo_apellido = request.data['segundo_apellido']
                numero_documento_identificacion = request.data['numero_documento_identificacion']
                password = request.data['password']

                user = Usuario()
                user.first_name = first_name
                user.last_name = first_lastname
                user.segundo_nombre = segundo_nombre
                user.segundo_apellido = segundo_apellido
                user.email = email
                user.username = email
                user.numero_documento_identificacion = numero_documento_identificacion

                user.is_active = True
                user.set_password(password)
                user.save()

                return Resp.send_response(_status=200, _msg='OK', _data="Usuario creado exitosamente")

        except Exception as e:
            print(3, 'Error, no se puede realizar login ' + str(e))
            return Resp.send_response(_status=503, _msg=ErrorMSG.get_msg(5003))


class logout(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            request.user.auth_token.delete()
            return Resp.send_response(_status=200, _msg='OK', _data="")
        except Exception as e:
            return Resp.send_response(_status=503, _msg=ErrorMSG.get_msg(5003))



@csrf_exempt
@api_view(['GET'])
def sample_api(request):
    username = request.user.username
    data = {'sample_data': 123, 'usuario': username}
    return Response(data, status=HTTP_200_OK)


class ObtenerUsuario(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication,)

    def get(self, request, format=None):
        try:
            username = request.user.username
            usuario = Usuario.objects.get(username=username)
            serializado = UsuarioSerializer(usuario)
            print('hOLAA')

            return Resp.send_response(_status=200, _msg='OK', _data=serializado.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg=ErrorMSG.get_msg(5003))