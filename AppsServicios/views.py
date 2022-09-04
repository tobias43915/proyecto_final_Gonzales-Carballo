# Create your views here.
from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Tecnologias
from AppsServicios.models import Contactos

#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

def contactos(request):

    return render(request, "AppsServicios/contactos.html")

    #Lista de tecnologias

def tecnologias(request):
    tecnologias= Tecnologias.objects.all()    
    return render(request, "AppsServicios/lista_tecnologia.html", {'tecnologias': tecnologias})

def tecnologia_formulario (request):
    if request.method =="POST":
        data_formulario: Dict = request.POST
        tecnologia= Tecnologias(nombre=data_formulario['nombre'], version=data_formulario['version'])
        Tecnologias.save
        return render(request, "AppsServicios/inicio.html")
    else:
        return render(request, "AppsServicios/form_tecnologias.html")
    