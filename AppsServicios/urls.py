#from django.contrib import path
from django.urls import path
from AppsServicios import views
#from AppsServicios import listar_tecnologias

urlpatterns =[
    
    path('',views.inicio, name = "inicio"),
    path('acerca-appsservices/',views.Acerca_nosotros,name="acerca_appsservices"),

#Urls Tecnologias

    path('tecnologias/',views.tecnologia,name= "tecnologias"),
    path('crear-tecnologia/',views.tecnologia_formulario, name= "tecnologia_formulario"),
    path('busqueda-tecnologia-form/', views.busqueda_tecnologia_form, name="busqueda_tecnologia_form"),
    path('buscar-tecnologia/', views.buscar, name="buscar-tecnologia"),
    path('eliminar-tecnologia/<int:id>/', views.eliminar_tecnologia, name="eliminar_tecnologia"),
    path('editar-tecnologia/<int:id>/', views.editar_tecnologia, name="editar_tecnologia"),
    
#Urls Contactos
    path('contactos/',views.contacto, name= "contactos"),
    path('crear-contacto/',views.contacto_formulario, name= "contacto_formulario"),
    path('eliminar-contacto/<int:id>/', views.eliminar_contacto, name="eliminar_contacto"),
    path('editar-contacto/<int:id>/', views.editar_contacto, name="editar_contacto"),

# Urls Servicios

    path('servicios/',views.servicio, name= "servicios"),
    path('crear-servicio/',views.servicio_formulario, name= "servicio_formulario"),
    path('eliminar-servicio/<int:id>/', views.eliminar_servicio, name="eliminar_servicio"),
    path('editar-servicio/<int:id>/', views.editar_servicio, name="editar_servicio"),
    

]

