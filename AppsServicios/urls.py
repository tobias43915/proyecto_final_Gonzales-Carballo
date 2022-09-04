#from django.contrib import path
from django.urls import path
#from AppsServicios.views import listar_Servicios
from AppsServicios.views import listar_tecnologias

urlpatterns =[
    
    path('',listar_tecnologias),
]

