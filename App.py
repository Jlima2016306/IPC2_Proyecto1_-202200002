import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from clases.Dato import Dato
from Listas.Lista_dato import Lista_dato
from Listas.Lista_senales import Lista_senales
from clases.Senal import Senal
from Listas.Lista_Cargador import Cargador_Dao



#Lectura del xml

Lista_senales_temporal= Lista_senales()
Cargador_Dao_list = Cargador_Dao()

ruta =askopenfilename()
archivo= open(ruta,"r")
archivo.close()



def cargador(self):

    
    ruta =askopenfilename()
    archivo= open(ruta,"r")
    archivo.close()

    tree = ET.parse(ruta)

    raiz=tree.getroot()

    
    







def imprimir_Lista():
    raiz = Cargador_Dao_list.devolver
    print(str(raiz))
    for senales_temporal in raiz.findall("senal"):
        nombre_Senal = senales_temporal.get("nombre")
        t_Senal = senales_temporal.get("t")
        A_Senal = senales_temporal.get("A")
        # Inicializamos listas
        Lista_dato_temporal= Lista_dato()
        Lista_dato_patrones_temporal= Lista_dato()

        for dato_senal in senales_temporal.findall("dato"):
            t_dato = dato_senal.get("t")
            A_dato = dato_senal.get("A")
            num_dato = dato_senal.text

            nuevo = Dato(int(t_dato), int(A_dato),int(num_dato))
            Lista_dato_temporal.insert_dato(nuevo)
            if num_dato != "NULL":
                nuevo = Dato(int(t_dato), int(A_dato),1)
                Lista_dato_patrones_temporal.insert_dato(nuevo)
            else:
                nuevo = Dato(int(t_dato), int(A_dato),0)
                Lista_dato_patrones_temporal.insert_dato(nuevo)                
        Lista_senales_temporal.Incertar_dato(Senal(nombre_Senal,t_Senal,A_Senal,Lista_dato_temporal,Lista_dato_patrones_temporal))
    
    Lista_senales_temporal.recorrer_e_imprimir_lista()



def mostrar_Documentarion():
    print("Julio Samuel Isaac Lima Donis")
    print("202200002")
    print("Introducción a la Programación y Computación 2 sección D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to semestre")



def mostrar_menu():
    print("")
    print("")
    print("-------Menú-----------")
    print("1. Cargar archivos")
    print("2. Procesar archivos ")
    print("3. Escribsir archivo salida")
    print("4. Mostrar Datos del estudiante")
    print("5. Generar Gráfica")
    print("6. Inicialializar")
    print("7. salir")
    opcion=input("Ingrese una opción del menú: ")
    while True:
        if opcion=="1":
            cargador()
        elif opcion=="2":
            imprimir_Lista() 
        elif opcion=="4":
             mostrar_Documentarion()
        elif opcion=="3":
             mostrar_Documentarion()
        elif opcion=="5":
            mostrar_Documentarion()
        elif opcion=="6":
            mostrar_Documentarion()
        elif opcion=="7":
            print("Saliendo del programa, vuevla pronto")
            exit()
        else:
            print("Indique una opción válida")
        mostrar_menu()
            

mostrar_menu()