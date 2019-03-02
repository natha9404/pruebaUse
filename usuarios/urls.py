from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login.as_view()),
    path('logout/', logout.as_view()),
    path('createUser/', createUser.as_view()),
    path('sampleapi/', sample_api)

]