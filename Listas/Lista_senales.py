from nodos.Nodo_senal import Nodo_senal
from Listas.grupo import grupo

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
        # recorremos la lista de carceles hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
        # Si entra al if, es por que encontramos la carcel que queremos
            if actual.senal.nombre==nombre_senal:
                actual=self.primero
       
                actual.senal.lista_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
                return
            actual=actual.siguiente
        print ("No se encontró la senal")


    def grafica_mi_lista_de_patrones(self,nombre_senal):
        actual=self.primero
        while actual != None:
        # Si entra al if, es por que encontramos la carcel que queremos
            if actual.senal.nombre==nombre_senal:
                actual=self.primero
       
                actual.senal.lista_patrones_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.t),
                                                    str(actual.senal.A))
                #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
                return
            actual=actual.siguiente
        print ("No se encontró la senal")
                
    def calcular_los_patrones(self,nombre_senal):
        # recorremos la lista de carceles hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
        # Si entra al if, es por que encontramos la carcel que queremos
            if actual.senal.nombre==nombre_senal:
                # Obtenemos sus patrones
                actual.senal.lista_patrones_nivel=actual.senal.lista_patrones_datos.devolver_patrones_por_nivel(actual.senal.lista_patrones_nivel)
                # Imprimimos todos sus patrones
                actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
                # obtenemos los grupos
                lista_patrones_temporal=actual.senal.lista_patrones_nivel
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                # Este es un string, por ejemplo "1,2--3,5--4"
                print(grupos_sin_analizar)
                # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
                #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
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

                    
                return
            actual=actual.siguiente
        print ("No se encontró la senal")


