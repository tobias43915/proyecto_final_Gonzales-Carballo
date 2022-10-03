import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppsServicios.models import Avatar

#from AppCoder.models import Avatar

class TecnologiaFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    version= forms.CharField(max_length=30)
    
class ContactosFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class ServicioFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    valor= forms.CharField(max_length=30)
    tiempo= forms.CharField(max_length=30)

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
