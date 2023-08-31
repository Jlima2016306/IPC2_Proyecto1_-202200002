from clases.Cargador import Cargador
from tkinter.filedialog import askopenfilename

class Cargador_Dao:
    def __init__(self,root):
        self.Cargador=[]






    def crear_producto(self,nombre):
        


        nuevo_producto = Cargador(nombre)
        self.Cargador.append(nuevo_producto)
        print("Se agrego un nuevo archivo")
        return  True    
    
    def devolver(self):
        return self.Cargador
    


