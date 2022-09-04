# Create your views here.
from ensurepip import version
from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Tecnologias
from AppsServicios.models import Contactos
from AppsServicios.models import Servicios
#from .AppsServicios.forms import NuevaTecnologia

#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

def contactos(request):

    return render(request, "AppsServicios/contactos.html")

    #Lista de tecnologias

def tecnologia(request):
    Tecnologia = Tecnologias.objects.all()    
    return render(request, "AppsServicios/lista_tecnologia.html")

def tecnologia_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        tecnologia = Tecnologias(nombre=data_formulario['nombre'], version=data_formulario['version'])
        tecnologia.save()

        return render(request, 'AppsServicios/inicio.html')
    else:
        return render(request, 'AppsServicios/form_tecnologias.html')


def servicio(request):
    Servicio = Servicios.objects.all()    
    return render(request, "AppsServicios/lista_servicios.html")


def servicio_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        servicio = Servicios(nombre=data_formulario['nombre'], tiempo=data_formulario['tiempo'], valor=data_formulario['valor'])
        servicio.save()

        return render(request, 'AppsServicios/inicio.html')
    else:
        return render(request, 'AppsServicios/form_servicios.html')

def contacto(request):
    Contacto = Contactos.objects.all()    
    return render(request, "AppsServicios/lista_contacto.html")

def contacto_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        contacto = Contactos(nombre=data_formulario['nombre'], apellido=data_formulario['apellido'], email=data_formulario['email'])
        contacto.save()

        return render(request, 'AppsServicios/inicio.html')
    else:
        return render(request, 'AppsServicios/form_contacto.html')