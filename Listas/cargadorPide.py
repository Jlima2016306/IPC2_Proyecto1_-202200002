
import tkinter as tk
from tkinter import filedialog


def select_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de Inventario", "*.inv")])
    root.destroy()  # Cierra la ventana de Tkinter después de seleccionar el archivo
    return file_path


if __name__ == "__main__":
    selected_file = select_file()
    if selected_file:
        print("Archivo seleccionado:", selected_file)
    else:
        print("Ningún archivo seleccionado.")