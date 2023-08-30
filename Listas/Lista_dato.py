from nodos.Nodo_dato import Nodo_dato
import sys
import os

class Lista_dato:
    def __init__(self):
        self.primero=None
        self.contador_dato=0
    
    def insert_dato(self,dato):
        if self.primero is None:
            self.primero = Nodo_dato(dato=dato)
            self.contador_dato+=1
            return
        actual = self.primero

        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=Nodo_dato(dato=dato)
        self.contador_dato+=1

    
    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual=self.primero
        while actual != None:
            print("Numero" ,actual.dato.num,"t",actual.dato.t,"A",actual.dato.A)
            

            actual=actual.siguiente
        print("============================================================")

            