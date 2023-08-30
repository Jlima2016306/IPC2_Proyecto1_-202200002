import tkinter as tk
from tkinter import filedialog
from Inventario_Dao import Inventario_Dao

manejador_Inventario = Inventario_Dao()


class cargador:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de Archivos")

        self.selected_file_label = tk.Label(root, text="Archivo seleccionado:")
        self.selected_file_label.pack(pady=10)

        self.file_path_label = tk.Label(root, text="")
        self.file_path_label.pack(pady=5)

        self.select_button = tk.Button(root, text="Seleccionar Archivo", command=self.select_file, command=self.root.close)
        self.select_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Inventario", "*.inv")])
        if file_path:
            self.file_path_label.config(text=file_path)
            #self.cargar_inventario(file_path)
            
            return file_path
        



 

if __name__ == "__main__":
    root = tk.Tk()
    app = cargador(root)
    root.mainloop()