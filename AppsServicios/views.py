# Create your views here.
from contextlib import redirect_stderr
from ensurepip import version
from typing import Dict
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Tecnologias
from AppsServicios.models import Contactos
from AppsServicios.models import Servicios
from AppsServicios.forms import TecnologiaFormulario

#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

#------------------------------------------Views tecnologias------------------------------#

def listar_tecnologias(request):
    queryset = Tecnologias.objects.all()
    diccionario={'AppsServicios': queryset}
    plantilla = loader.get_template('lista_tecnologias.html')
    documento_html = plantilla.render(diccionario)
       
    return HttpResponse(documento_html)

def tecnologia(request):
    tecnologia = Tecnologias.objects.all()
    #--------------------------nuevo 1709-----------------------------
    borrado = request.GET.get('borrado', None)
    contexto= {'tecnologia':tecnologia}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/lista_tecnologias.html",contexto)

def tecnologia_formulario(request):
    if request.method == 'POST':
        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            tecnologia = Tecnologias(nombre=data['nombre'], version=data['version'])
            tecnologia.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = TecnologiaFormulario()  
    return render(request, 'AppsServicios/form_tecnologias.html', {"formulario": formulario})

#-------------------------busqueda---------------------------------
def busqueda_tecnologia_form(request):
      return render(request, "AppsServicios/form_buscar.html")

def buscar(request):
      if request.GET["tecnologia"]:
            tecnologia = request.GET["tecnologia"]
            tecnologia = Tecnologias.objects.filter(tecnologia__icontains=tecnologia)
            return render(request, "AppsServicios/inicio.html", {'tecnologia': tecnologia})
      
      else:

        respuesta= "No ingresaste informacion"
        
        return render(request, "AppsServicios/inicio.html", {'respuesta':respuesta})

#-------------------------------------------nuevo 1709 elimina tecno-----------------------

def eliminar_tecnologia(request, id):
    tecnologia = Tecnologias.objects.get(id=id)
    borrado_id = tecnologia.id
    tecnologia.delete()
    url_final = f"{reverse('tecnologias')}?borrado={borrado_id}"
    return redirect(url_final)

#E-----------------------------ditar las tecnologias 1709----------------------------------------

def editar_tecnologia(request, id):

    tecnologia = Tecnologias.objects.get(id=id)

    if request.method == 'POST':
        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            tecnologia.nombre = data['Nombre']
            tecnologia.version = data['Version']
            tecnologia.save()

            return redirect(reverse('tecnologias'))

    else:  # GET
        inicial = {
            'nombre': tecnologia.nombre,
            'version': tecnologia.version,
        }
        formulario = TecnologiaFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_tecnologias.html', {"formulario": formulario})

#----------------------------------Views servicios------------------------------------------------------#

def servicio(request):
    servicio = Servicios.objects.all()    
    return render(request, "AppsServicios/lista_servicios.html",{'servicio':servicio})

def servicio_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        servicio = Servicios(nombre=data_formulario['nombre'], tiempo=data_formulario['tiempo'], valor=data_formulario['valor'])
        servicio.save()

        return render(request, 'AppsServicios/inicio.html',{"exitoso": True})
    else:
        return render(request, 'AppsServicios/form_servicios.html')


#---------------------------------views contactos------------------------------------------------------#

def contacto(request):
    contacto = Contactos.objects.all()    
    return render(request, "AppsServicios/contactos.html")

def contacto_formulario(request):

    if request.method == 'POST':
        data_formulario: Dict = request.POST
        contacto = Contactos(nombre=data_formulario['nombre'], apellido=data_formulario['apellido'], email=data_formulario['email'])
        contacto.save()

        return render(request, 'AppsServicios/inicio.html',{"exitoso": True})
    else:
        return render(request, 'AppsServicios/form_contacto.html')
