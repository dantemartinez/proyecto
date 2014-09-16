#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *

class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("proyecto.ui",self)
        self.filename="guardar.ini"
        self.cont=0
        self.cargarLista()

    def yaExisteDni(self, dni):
        f = self.getFile()
        for line in f:
            datos = line.split(",")
            if datos[5]==dni:
                f.close()
                return True
        f.close()
        return False

    def guardar(self):
        self.nombre = self.ui.Nombre.text()
        self.apellido = self.ui.Apellido.text()
        self.nacimiento = self.ui.FechaNac.text()
        self.curso = self.ui.Curso.text()
        self.division = self.ui.Division.text()
        self.dni = self.ui.Dni.text()
        if (not self.yaExisteDni(self.dni)):
            value=self.nombre+","+self.apellido+","+self.nacimiento+","+self.curso+","+self.division+","+self.dni+","
            f = open(self.filename, "a")
            f.write(value)
            f.close()
            self.ui.Nombre.setText("")
            self.ui.Apellido.setText("")
            self.ui.FechaNac.setText("")
            self.ui.Curso.setText("")
            self.ui.Division.setText("")
            self.ui.Dni.setText("")
            self.cargarLista()
            self.ui.lblResultados.setText("Guardado")
        else:
            self.ui.lblResultados.setText("Dni Duplicado")

    def ver(self):
        f = self.getFile()
        dniCargado=self.ui.cmbDni.currentText()
        for line in f:
            datos = line.split(",")
            if datos[5]==dniCargado:
                self.ui.D.setText(datos[6])
                self.ui.P.setText(datos[7])
                self.ui.PC.setText(datos[8])
                return

    def cargarLista(self):
        f = self.getFile()
        isEnd = False
        print f
        count=0
        self.ui.cmbDni.clear()
        self.ui.cmbDni2.clear()
        self.ui.cmbDni.insertItem(count,"Seleccionar")
        self.ui.cmbDni2.insertItem(count,"Seleccionar")
        for line in f:
            datos = line.split(",")
            count = count+1
            self.ui.cmbDni.insertItem(count,str(datos[5]))
            self.ui.cmbDni2.insertItem(count,str(datos[5]))
        f.close()

    def getFile(self):
        try:
            f=open(self.filename, "r")
        except:
            f=open(self.filename, "w")
        return f

    def funcion(self):
        llamo=self.sender().text()

    def continuar(self):
        self.cont+=1
        if (self.cont<=2):
            self.ui.tabWidget.setCurrentIndex(self.cont)

    def limpiar(self):
        self.ui.lista.clear()

    def limpiar2(self):
        self.ui.lista2.clear()

    def guardar2(self):
        cuotasdebe=self.ui.D.text()
        cuotaspago=self.ui.P.text()
        cuotascosto=self.ui.PC.text()
        value=cuotasdebe+","+cuotaspago+","+cuotascosto+"\n"
        f = open(self.filename, "a")
        f.write(value)
        f.close()
        self.ui.D.setText("")
        self.ui.P.setText("")
        self.ui.PC.setText("")
        self.cargarLista()

    def aceptar(self):
        self.debe=self.ui.D.text()
        self.pago=self.ui.P.text()
        self.costo=self.ui.PC.text()
        self.ui.lista.addItem("Debe: $"+str(int(self.costo)*int(self.debe)))
        self.ui.lista.addItem("Pago: $"+str(int(self.costo)*int(self.pago)))

    def mostrar(self):
        f = self.getFile()
        dniCargado=self.ui.cmbDni2.currentText()
        for line in f:
            datos = line.split(",")
            if datos[5]==dniCargado:
                self.ui.lista2.addItem("Nombre: "+datos[0])
                self.ui.lista2.addItem("Apellido: "+datos[1])
                self.ui.lista2.addItem("Fecha de nacimiento: "+datos[2])
                self.ui.lista2.addItem("Curso: "+datos[3]+" "+datos[4])
                self.ui.lista2.addItem("DNI: "+datos[5])
                self.ui.lista2.addItem("Cuotas que debe: "+datos[6])
                self.ui.lista2.addItem("Debe un total de: $"+str(int(self.costo)*int(self.debe)))
                self.ui.lista2.addItem("Cuotas que pago: "+datos[7])
                self.ui.lista2.addItem("Pago un total de: $"+str(int(self.costo)*int(self.debe)))

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Myform()
    myapp.show()
    sys.exit(app.exec_())
