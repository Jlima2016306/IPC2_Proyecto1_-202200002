from clases.Cargador import Cargador
from tkinter.filedialog import askopenfilename
from nodos.nodo_c import Nodo_c

class Cargador_Dao:
    def __init__(self,root):

        self.primero=None





    def crear_producto(self,c):

    
        if self.primero is None:
            self.primero =Nodo_c(c=c)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= Nodo_c(c=c)
        print("Se agrego un nuevo archivo")

    
    
    def devolver(self):
        actual = self.primero
        return actual
    
    def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None 
    


