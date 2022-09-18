from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from AppCoder.models import Avatar

class TecnologiaFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    version= forms.CharField(max_length=30)
   