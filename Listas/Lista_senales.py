from nodos.Nodo_senal import Nodo_senal
from Listas.grupo import grupo
import xml.etree.ElementTree as ET
import os

class Lista_senales:
    def __init__(self):
        self.primero=None
        self.contador_senales=0
    
    def Incertar_dato(self,senal):
        if self.primero is None:
            self.primero =Nodo_senal(senal=senal)
            self.contador_senales+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= Nodo_senal(senal=senal)
        self.contador_senales+=1
    
    def recorrer_e_imprimir_lista(self):
        print("Total de senales almacenadas:",self.contador_senales)
        print("")
        print("")
        print("")
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            
            print("Nombre",actual.senal.nombre,"t:",actual.senal.t,"A:",actual.senal.A)
            actual.senal.lista_datos.recorrer_e_imprimir_lista()
            actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
            actual= actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("")
        print("")
        print("")     


    def grafica_mi_lista_original(self,nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre_senal:
                
       
                actual.senal.lista_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                return
            actual=actual.siguiente
        print ("No se encontró la senal")


    def grafica_mi_lista_de_patrones(self,nombre_senal):
        actual=self.primero
        while actual != None:
            if actual.senal.nombre==nombre_senal:
       
                actual.senal.lista_patrones_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                return
            actual=actual.siguiente
        print ("No se encontró la senal")


    def grafica_mi_lista_Reducida(self,nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre_senal:
                actual.senal.lista_grupos.recorrer_e_imprimir_lista()

                actual.senal.lista_grupos.generar_graficaBIN(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                return
            actual=actual.siguiente
        print ("No se encontró la senal")
                
    def calcular_los_patrones(self,nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre_senal:
                actual.senal.lista_patrones_nivel=actual.senal.lista_patrones_datos.devolver_patrones_por_nivel(actual.senal.lista_patrones_nivel)
                lista_patrones_temporal=actual.senal.lista_patrones_nivel
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                print(grupos_sin_analizar)
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.senal.lista_grupos.insertar_dato(grupo=grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer_e_imprimir_lista()
                actual.senal.lista_grupos.generar_graficaBIN(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                    
                return
            actual=actual.siguiente
        print ("No se encontró la senal")



    def generar_xml_salida(self,ruta):
        contador = 0
        try:
            if os.path.exists(ruta):

                mis_senales= ET.Element("senalesReducidas")
                lista_senales= ET.SubElement(mis_senales,"listaSenales")
                actual= self.primero
                while actual !=None:
                    senal= ET.SubElement(lista_senales,"senal nombre="+"'"+actual.senal.nombre+"'"+" A="+"'"+actual.senal.A+"'")
                    nombre=ET.SubElement(senal,"nombre")
                    nombre.text=actual.senal.nombre 
                    

                    contador+=1
                    actual_lista_patrones=actual.senal.lista_patrones_datos.primero
                    lista_patrones=ET.SubElement(senal,"grupo g="+"'"+str(contador)+"'")   
                    tiempo= ET.SubElement(lista_patrones,"tiempo")
                    tiempo.text=str(actual.senal.t)
                    while actual_lista_patrones!=None:
                        dato=ET.SubElement(lista_patrones,"dato")
                        dato.text=str(actual_lista_patrones.dato.num)
                        actual_lista_patrones=actual_lista_patrones.siguiente
                    actual=actual.siguiente      

                my_data=ET.tostring(lista_senales)
                my_data=str(my_data)        
                self.xml_arreglado(lista_senales)
                print("válidado y creado")

                arbol_xml=ET.ElementTree(lista_senales)
                arbol_xml.write(ruta,encoding="UTF-8",xml_declaration=True)        

            else:
                print(f"La ruta '{ruta}' no existe.")
        except Exception as e:
                print(f"Hubo un error al verificar la ruta: {str(e)}")


    def xml_arreglado(self, element, indent='  '):

        queue = [(0, element)] 
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children




    def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None 