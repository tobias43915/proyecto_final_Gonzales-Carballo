#from django.contrib import path
from django.urls import path
from AppsServicios import views

urlpatterns =[
    
    path('',views.inicio, name = "inicio"),
    path('tecnologias/',views.tecnologia, name= "tecnologias"),
    path('contactos/',views.contactos, name= "contactos"),
    path('crear-tecnologia/',views.tecnologia_formulario, name= "tecnologia_formulario"),
    path('crear-servicio/',views.servicio_formulario, name= "servicio_formulario"),
    path('crear-contacto/',views.contacto_formulario, name= "contacto_formulario"),
]

