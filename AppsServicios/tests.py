import random
import string
#from typing_extensions import Self

from django.test import TestCase
from AppsServicios.models import Tecnologias, Servicios, Contactos

#class TecnologiasTestCase(TestCase):
#
#        def test_creacion_tecnologias(self):
#                #Test 1: Comprobar puedo crear un profesor con un nombre con letras random
#                lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
#                print(lista_letras_nombre)
#                lista_letras_version = [random.choice(string.ascii_letters + string.digits) for _ in range(10)]
#                nombre_prueba = "".join(lista_letras_nombre)
#                version_prueba = "".join(lista_letras_version)
#                print(nombre_prueba)
#                print(version_prueba)
#                Tecnologias_1 = Tecnologias.objects.create(nombre=nombre_prueba,version=version_prueba)

#                self.assertIsNotNone(Tecnologias_1.id)
#                self.assertEqual(Tecnologias_1.nombre, nombre_prueba)
#                self.assertEqual(Tecnologias_1.version, version_prueba)




#class ServiciosTestCase(TestCase):
#
#        def test_creacion_servicios(self):
#                #Test 1: Comprobar puedo crear un profesor con un nombre con letras random
#                lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
#                print(lista_letras_nombre)
#                lista_letras_tiempo = [random.choice(string.ascii_letters + string.digits) for _ in range(4)]
#                lista_numeros_valor = [random.choice(str(12) + str(5)) for  _ in range(10)]
#                nombre_prueba = "".join(lista_letras_nombre)
#                tiempo_prueba = "".join(lista_letras_tiempo)
#                valor_prueba = "".join(lista_numeros_valor)
#                print(nombre_prueba)
#                print(tiempo_prueba)
#                print(valor_prueba)
#                Servicios_1 = Servicios.objects.create(nombre=nombre_prueba,tiempo=tiempo_prueba,valor=valor_prueba)

#                self.assertIsNotNone(Servicios_1.id)
#                self.assertEqual(Servicios_1.nombre, nombre_prueba)
#                self.assertEqual(Servicios_1.tiempo, tiempo_prueba)
#                self.assertEqual(Servicios_1.valor, valor_prueba)


class ContactosTestCase(TestCase):

        def test_creacion_contactos(self):
                #Test 1: Comprobar puedo crear un contacto con un nombre con letras random
                lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
                print(lista_letras_nombre)
                lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(4)]
                lista_email = [str("prueba@example.com")]
                nombre_prueba = "".join(lista_letras_nombre)
                apellido_prueba = "".join(lista_letras_apellido)
                email_prueba = "".join(lista_email)
                print(nombre_prueba)
                print(apellido_prueba)
                print(email_prueba)
                Contactos_1 = Contactos.objects.create(nombre=nombre_prueba,apellido=apellido_prueba,email=email_prueba)

                self.assertIsNotNone(Contactos_1.id)
                self.assertEqual(Contactos_1.nombre, nombre_prueba)
                self.assertEqual(Contactos_1.apellido, apellido_prueba)
                self.assertEqual(Contactos_1.email, email_prueba)