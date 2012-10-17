#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys

pilas.iniciar()

fondo = pilas.fondos.Fondo("fondo.jpg")
fondo.escala = 0.7

posicionV = 10
posicionL = -170
posicionR = 30
lblEscala = 0.75
escapar = 500
# Boton
boton = pilas.interfaz.Boton("Enviar")
boton.x,boton.y = 100,-10

def cuando_hacen_click():
    lblNombre.x = [lblNombre.x,escapar]
    txtNombre.x = [txtNombre.x,-escapar]
    txtApellido.x = [txtApellido.x,escapar]
    lblApellido.x = [lblApellido.x,-escapar]
    lblSexo.x = [lblSexo.x,escapar]
    opcionesSexo.y = [boton.y, -600]
    opcionesSexo.rotacion=[0,-360]
    lblEdad.x = [lblEdad.x,escapar]
    lblEdadTotal.x = [lblEdadTotal.x,-escapar]
    edad.x = [edad.x,-escapar]
    boton.aprender(pilas.habilidades.PuedeExplotar)
    boton.eliminar()
    lblGracias = pilas.actores.Texto("MUCHAS GRACIAS!!!")
    pilas.avisar(u'Se envió el formulario')

boton.conectar(cuando_hacen_click)



# Entrada de texto
lblNombre = pilas.actores.Texto("Nombre:")
lblNombre.escala = lblEscala
lblNombre.x,lblNombre.y = posicionL,(posicionV *20)
txtNombre = pilas.interfaz.IngresoDeTexto()
txtNombre.texto = ""
txtNombre.x,txtNombre.y = posicionR,(posicionV *20)

lblApellido = pilas.actores.Texto("Apellido:")
lblApellido.escala = lblEscala
lblApellido.x,lblApellido.y = posicionL,(posicionV *15)
txtApellido = pilas.interfaz.IngresoDeTexto()
txtApellido.texto = ""
txtApellido.x,txtApellido.y = posicionR,(posicionV *15)

# Lista de selecciï¿½n
def cuando_selecciona_sexo(opcion_seleccionada):
    #pilas.avisar("Ha seleccionado la opcion: " + opcion_seleccionada)
    return None


lblSexo = pilas.actores.Texto("Sexo:")
lblSexo.escala = lblEscala
lblSexo.x,lblSexo.y = posicionL,(posicionV *10)
opcionesSexo = pilas.interfaz.ListaSeleccion(['Varon', 'Mujer',''], cuando_selecciona_sexo)
opcionesSexo.x,opcionesSexo.y = posicionR-100,(posicionV *10)


lblEdad = pilas.actores.Texto("Edad:")
lblEdad.escala = lblEscala
lblEdad.x,lblEdad.y = posicionL,(posicionV * 5)
lblEdadTotal = pilas.actores.Texto(u'0 años')
lblEdadTotal.escala = lblEscala
lblEdadTotal.x,lblEdadTotal.y = posicionL + 2 + lblEdad.ancho,(posicionV * 5)


def cuando_cambia_edad(valor):
	lblEdadTotal.definir_texto(str(int(valor * 100)) +u' años') 

edad = pilas.interfaz.Deslizador()
edad.conectar(cuando_cambia_edad)
edad.x,edad.y = posicionR,posicionV*5

# Selector
'''
sexoMasculino = pilas.interfaz.Selector("Masculino", x=-30, y=posicionV*10)
sexoFemenino = pilas.interfaz.Selector("Femenino", x=100, y=posicionV*10)

sexoFemenino.alternar_seleccion() = None
sexoMasculino.alternar_seleccion() = None

sexoMasculino.seleccionar()
def selMasculino(estado):
    if(estado):
        sexoFemenino.deseleccionar()
    else:
        sexoFemenino.seleccionar()

def selFemenino(estado):
    if(estado):
        sexoMasculino.deseleccionar()
    else:
        sexoMasculino.seleccionar()


sexoFemenino.definir_accion(selFemenino(sexoFemenino.seleccionado))
sexoMasculino.definir_accion(selMasculino(sexoMasculino.seleccionado))
'''


pilas.ejecutar()
