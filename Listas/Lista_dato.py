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
        i=0
        print("No.","Nom","t","A")
        while actual != None:
            print(i,actual.dato.num,actual.dato.t,actual.dato.A)
            actual=actual.siguiente

            

            

            i+=1
        print("============================================================")

            

    def generar_grafica(self,num,t,dato_por_nivel):
        f = open('bb.dot','w')
        text ="""
            digraph G {"niveles="""+t+"""","CeldasNivel="""+dato_por_nivel+""""->" """+num+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""        
        actual = self.primero
        sentinela_de_filas=actual.dato.t #iniciaria en 1
        fila_iniciada=False
        while actual != None: 
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.dato.t:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.dato.t
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.num)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.num)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o 17agosto.png')
        print("terminado")
