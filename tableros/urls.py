from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('crear_tablero/', CrearTablero.as_view()),
    path('crear_tarjeta/', CrearTarjeta.as_view()),
    path('listarTableroPublicos/', ListarTablerosPublicos.as_view()),
    path('listarTablerosUsuario/', ListarTablerosUsuario.as_view()),
    path('listarTarjetasTablero/', ListarTarjetasTablero.as_view()),
    path('modificarTarjeta/', ActualizarTarjeta.as_view()),
    path('listar_solicitudes/', ListarSolicitudes.as_view()),
    path('aprobar_solicitudes/', AceptarSolicitud.as_view()),

]