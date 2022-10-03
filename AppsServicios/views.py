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
from AppsServicios.forms import TecnologiaFormulario,ContactosFormulario
from AppsServicios.forms import ServicioFormulario
from AppsServicios.forms import AvatarFormulario
from AppsServicios.forms import UserUpdateForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/plantilla_base.html")
#Views de acerca de nosotros 

def Acerca_nosotros(request):

    return render(request, "AppsServicios/Acerca_AppsServices.html")

def about(request):

    return render(request, "AppsServicios/about.html")
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
@login_required
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
#def busqueda_tecnologia_form(request):
 #     return render(request, "AppsServicios/resultado_busqueda_tecnologia.html")
#form_buscar

def buscartecnologia(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        tecnologia = Tecnologias.objects.filter(nombre__icontains=nombre)
        return render(request, "AppsServicios/resultado_busqueda_tecnologia.html", {'tecnologia':tecnologia,'nombre': nombre})
    else:
        resultado = "No hay resultados"

        #return HttpResponse(resultado)
        
        return render(request, "AppsServicios/inicio.html", {'resultado':resultado})

#-------------------------------------------nuevo 1709 elimina tecno-----------------------
@login_required
def eliminar_tecnologia(request, id):
    tecnologia = Tecnologias.objects.get(id=id)
    borrado_id = tecnologia.id
    tecnologia.delete()
    url_final = f"{reverse('tecnologias')}?borrado={borrado_id}"
    return redirect(url_final)

#E-----------------------------ditar las tecnologias 1709----------------------------------------
@login_required
def editar_tecnologia(request, id):

    tecnologia = Tecnologias.objects.get(id=id)

    if request.method == 'POST':
        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            tecnologia.nombre = data['nombre']
            tecnologia.version = data['version']
            tecnologia.save()

            return redirect('tecnologias')

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
    borrado = request.GET.get('borrado', None)
    contexto= {'servicio':servicio}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/lista_servicios.html",contexto)
    
#---------------------form servicio--------------------------
@login_required
def servicio_formulario(request):
    if request.method == 'POST':
        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            servicio = Servicios(nombre=data['nombre'], valor=data['valor'],tiempo=data['tiempo'])
            servicio.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = ServicioFormulario()  
    return render(request, 'AppsServicios/form_servicios.html', {"formulario": formulario})

#----------------------------eliminar servicio-----------------
@login_required
def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    borrado_id = servicio.id
    servicio.delete()
    url_final = f"{reverse('servicios')}?borrado={borrado_id}"
    return redirect(url_final)
#------------------------editar servicios------------------
@login_required
def editar_servicio(request, id):

    servicio = Servicios.objects.get(id=id)

    if request.method == 'POST':
        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            servicio.nombre = data['nombre']
            servicio.valor = data['valor']
            servicio.tiempo = data['tiempo']
            servicio.save()

            return redirect(reverse('servicios'))

    else:  # GET
        inicial = {
            'nombre': servicio.nombre,
            'valor': servicio.valor,
            'tiempo': servicio.tiempo,
        }
        formulario = ServicioFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_servicios.html', {"formulario": formulario})

#---------------------------------views contactos------------------------------------------------------#

def contacto(request):
    contacto = Contactos.objects.all()
    borrado = request.GET.get('borrado', None)
    contexto= {'contacto':contacto}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/contactos.html",contexto)
@login_required
def contacto_formulario(request):
    if request.method == 'POST':
        formulario = ContactosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            contacto = Contactos(nombre=data['nombre'], apellido=data['apellido'],email=data['email'])
            contacto.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = ContactosFormulario()  
    return render(request, 'AppsServicios/form_contacto.html', {"formulario": formulario})

#--------------------------------------eliminar contacto------------------
@login_required
def eliminar_contacto(request, id):
    contacto = Contactos.objects.get(id=id)
    borrado_id = contacto.id
    contacto.delete()
    url_final = f"{reverse('contactos')}?borrado={borrado_id}"
    return redirect(url_final)

#----------------editar---------------
@login_required
def editar_contacto(request, id):

    contacto = Contactos.objects.get(id=id)

    if request.method == 'POST':
        formulario = ContactosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            contacto.nombre = data['nombre']
            contacto.apellido = data['apellido']
            contacto.email = data['email']
            contacto.save()

            return redirect(reverse('contactos'))

    else:  # GET
        inicial = {
            'nombre': contacto.nombre,
            'apellido': contacto.apellido,
            'apellido': contacto.email,
        }
        formulario = ContactosFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_contacto.html', {"formulario": formulario})



#------------------------------------------- Envío de Email--------------------------------------------
def contacto_por_email(request):
    if request.method == "POST":
        name = request.POST["nombre"]
        email = request.POST["email"]
        subject = request.POST["asunto"]
        message = request.POST["mensaje"]

        template = render_to_string('AppsServicios/Email.html', {'name': name, 'email': email, 'message': message})
        
        email = EmailMessage(subject, template, settings.EMAIL_HOST_USER, ['app_services@gmail.com'])

        email.fail_silently = False
        email.send()
        
        messages.success(request, 'Se ha enviado su consulta')
        return redirect("AppsServicios/contacto_email.html")
    else:
        #try:
            #avatar = Avatar.objects.get(usuario = request.user.id)
         #   return render(request, "09 - Contacto.html", {"url": avatar.imagen.url})
        #except: render
            return render(request, "AppsServicios/contacto_email.html")


#----------------------------Registro de usuario------------------------------------------

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppsServicios/Inicio.html", {"mensaje": f'Usuario {username} creado'})

    else:
        form = UserCreationForm()

    return render(request, "AppsServicios/registro.html", {"formulario": form})

#---------------------------------------------Login--------------------------------------
def Loginview(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            user = authenticate(username=usuario, password=psw)
            if user:
                login(request, user=user)
                if next_url:
                    return render(request, "AppsServicios/inicio.html", {"mensaje": f'Bienvenido/a {usuario}'})
            else:
                return render(request, "AppsServicios/inicio.html", {"mensaje": 'Datos incorrectos'})

        return render(request, "AppsServicios/inicio.html",{"mensaje": "error, formulario"})

    else:
        formulario = AuthenticationForm()
    return render(request, "AppsServicios/login.html", {"formulario": formulario})


@login_required
def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "AppsServicios/form_avatar.html", {"form":form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'AppsServicios/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
