#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pilas


pilas.iniciar(titulo='Formulario')


class Formulario:
    '''Genera un ejemplo de formulario hecho en pilas-engine'''

    def __init__(self):
        '''Es la funcion lider, que se ejecutara al ser llamada la clase "Formulario"'''
        self.magnitud = 17  # es la variable que usaran los textos para definir su magnitud
        self.fondo = pilas.fondos.Fondo('fondo.jpg')  # se elige un fondo
        self.fondo.escala = 0.7  # cambiamos la escala
        self.crear_formulario()
        
    def crear_formulario(self):
        '''Se encarga de crear los elementos del formulario'''
        self.lblNombre = pilas.actores.Texto(texto='Nombre:', magnitud=self.magnitud, x=-170, y=200)
        self.txtbNombre = pilas.interfaz.IngresoDeTexto(x=30, y=200)
        self.lblApellido = pilas.actores.Texto(texto='Apellido:', magnitud=self.magnitud, x=-170, y=150)
        self.txtbApellido = pilas.interfaz.IngresoDeTexto(x=30, y=150)
        self.lblSexo = pilas.actores.Texto(texto='Sexo:', magnitud=self.magnitud, x=-170, y=100)
        
        def selecciona_sexo(opcion): return None
        
        self.lstSexo = pilas.interfaz.ListaSeleccion(['Varon', 'Mujer',''], selecciona_sexo, x=-70, y=100)
        self.lblEdad = pilas.actores.Texto(texto='Edad:', magnitud=self.magnitud, x=-170, y=50)
        self.lblEdadTotal = pilas.actores.Texto(texto=u'0 años', magnitud=self.magnitud, x=(-160 + self.lblEdad.ancho), y=50)
        self.dslEdad = pilas.interfaz.Deslizador(x=30, y=50)
        
        def cambia_edad(valor):
            '''Genera un cambio de edad en base al deslizador'''
            self.lblEdadTotal.definir_texto(str(int(valor * 100)) +u' años')
             
        self.dslEdad.conectar(cambia_edad)
        self.boton = pilas.interfaz.Boton(texto='Enviar', x=100, y=-10)
        
        def pulsa():
            '''Saca de la escena el formulario y da un mensaje de envio'''
            self.lblNombre.x = [-500]
            self.txtbNombre.x = [500]
            self.lblApellido.x = [-500]
            self.txtbApellido.x = [500]
            self.lblSexo.x = [-500]
            self.lstSexo.y = [-500]
            self.lstSexo.rotacion = [-360]
            self.lblEdad.x = [-500]
            self.lblEdadTotal.x = [500]
            self.dslEdad.x = [-500]
            self.boton.aprender(pilas.habilidades.PuedeExplotar)
            self.boton.eliminar()
            self.lblGracias = pilas.actores.Texto('MUCHAS GRACIAS!!!')
            pilas.avisar(u'Se envió el formulario')

        self.boton.conectar(pulsa)



Formulario()

pilas.ejecutar()