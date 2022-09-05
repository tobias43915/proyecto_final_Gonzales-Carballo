# Create your views here.
from ensurepip import version
from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Tecnologias
from AppsServicios.models import Contactos
from AppsServicios.models import Servicios


#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

    #Lista de tecnologias

def listar_tecnologias(request):
    queryset = Tecnologias.objects.all()
    diccionario={'AppsServicios': queryset}
    plantilla = loader.get_template('lista_tecnologias.html')
    documento_html = plantilla.render(diccionario)
       
    return HttpResponse(documento_html)

def contactos(request):

    return render(request, "AppsServicios/contactos.html")

def tecnologia(request):
    Tecnologia = Tecnologias.objects.all()    
    return render(request, "AppsServicios/lista_tecnologias.html")

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
    return render(request, "AppsServicios/contactos.html")

def contacto_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        contacto = Contactos(nombre=data_formulario['nombre'], apellido=data_formulario['apellido'], email=data_formulario['email'])
        contacto.save()

        return render(request, 'AppsServicios/inicio.html')
    else:
        return render(request, 'AppsServicios/form_contacto.html')