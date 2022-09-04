#from django.contrib import path
from django.urls import path
#from AppsServicios.views import listar_Servicios
#from AppsServicios.views import listar_tecnologias
#from AppsServicios.views import lista_contactos
from AppsServicios import views

urlpatterns =[
    
    path('',views.inicio, name = "inicio"),
    path('tecnologias/',views.tecnologias, name= "tecnologias"),
    path('contactos/',views.contactos, name= "contactos"),
    path('crear-tecnologia/',views.tecnologia_formulario, name= "tecnologia_formulario"),
]

