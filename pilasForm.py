# -*- encoding: utf-8 -*-
import pilas
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys

pilas.iniciar()
posicionV = 10
posicionL = -170
posicionR = 30
lblEscala = 0.75
# Boton
boton = pilas.interfaz.Boton("Enviar")
boton.x,boton.y = -200,-200

def cuando_hacen_click():
    pilas.avisar("Se envía el formulario")

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

# Selector

sexoMasculino = pilas.interfaz.Selector("Masculino", x=-30, y=posicionV*10)
sexoFemenino = pilas.interfaz.Selector("Femenino", x=100, y=posicionV*10)
sexoMasculino.seleccionar
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


sexoFemenino.cuando_hace_click(selFemenino(sexoFemenino.estado))
sexoMasculino.cuando_hace_click(selMasculino(sexoMasculino.estado))

pilas.ejecutar()
