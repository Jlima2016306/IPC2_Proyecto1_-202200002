from nodos.Nodo_senal import Nodo_senal


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
        while actual != None:
            print("Nombre",actual.senal.nombre,"t:",actual.senal.t,"A:",actual.senal.A)
            actual.senal.lista_datos.recorrer_e_imprimir_lista()
            actual= actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("")
        print("")
        print("")            