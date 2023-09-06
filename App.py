import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import filedialog

from clases.Dato import Dato
from Listas.Lista_dato import Lista_dato
from Listas.Lista_senales import Lista_senales
from clases.Senal import Senal
from Listas.Lista_Cargador import Cargador_Dao

from Listas.lista_patrones import lista_patrones
from Listas.lista_grupos import lista_grupos

#Lectura del xml

Lista_senales_temporal= Lista_senales()
Cargador_Dao_list = Cargador_Dao(0)
#Cargador_Dao_list = Cargador_Dao()


def cargador():
    
    ruta =askopenfilename()

    if ruta != "" :
        archivo= open(ruta,"r")
        archivo.close()

        # Parsear para que nuestra aplicación entienda que manipulará xml
        tree = ET.parse(ruta)
        raiz=tree.getroot()
        print(str(raiz))
        Cargador_Dao_list.crear_producto(raiz)

        raiz = Cargador_Dao_list.devolver()
        print("Archivo Cargado")
        
    else:
        print("No eligio un archivo")

    
    







def imprimir_Lista():
    print("Procesando archivos...")
    raiz = Cargador_Dao_list.devolver()
    raizVerde =Cargador_Dao_list.devolver()

    
   
    if raizVerde:
        print("Obteniendo las senales_temporal...")
        for senales_temporal in raiz.c.findall("senal"):
            print("Procesando la senal"+senales_temporal.get("nombre")+"...")
            nombre_Senal = senales_temporal.get("nombre")
            t_Senal = senales_temporal.get("t")
            A_Senal = senales_temporal.get("A")
            # Inicializamos listas
            Lista_dato_temporal= Lista_dato()
            Lista_dato_patrones_temporal= Lista_dato()

            lista_patrones_temporal=lista_patrones()

            lista_grupos_temporal=lista_grupos()
            for dato_senal in senales_temporal.findall("dato"):
                print("Calculando las matrices...")
                t_dato = dato_senal.get("t")
                A_dato = dato_senal.get("A")
                num_dato = dato_senal.text
                if dato_senal.text == "NULL":
                    num_dato = 0

                nuevo = Dato(int(t_dato), int(A_dato),int(num_dato))
                Lista_dato_temporal.insertar_dato(nuevo)
                if num_dato != "NULL" and int(num_dato) >0:
                    nuevo = Dato(int(t_dato), int(A_dato),1)
                    Lista_dato_patrones_temporal.insertar_dato(nuevo)
                else:
                    nuevo = Dato(int(t_dato), int(A_dato),0)
                    Lista_dato_patrones_temporal.insertar_dato(nuevo)                
            Lista_senales_temporal.Incertar_dato(Senal(nombre_Senal,t_Senal,A_Senal,Lista_dato_temporal,Lista_dato_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal))
            print("Matrices ok!")
        
    else:
        print("Sin archivos")


def graficar():
    print("Elija que tipo de grafica quiere:")
    print("1. Normal")
    print("2. Patrones ")
    print("3. Reducida")
    print("4. Salir ")
    opcion=input("Ingrese una opción del menú: ")
    while True:
        if opcion=="1":
            opcion2=input("Escriba el nombre de la señal: ")
            Lista_senales_temporal.grafica_mi_lista_original(opcion2)            
        elif opcion=="2":
            opcion2=input("Escriba el nombre de la señal: ")
            Lista_senales_temporal.grafica_mi_lista_de_patrones(opcion2) 
        elif opcion=="3":
            opcion3=input("Escriba el nombre de la señal: ")
            Lista_senales_temporal.calcular_los_patrones(opcion3) 
        elif opcion=="4":
             mostrar_menu()

        else:
            print("Indique una opción válida")
            graficar()
        mostrar_menu()


def generar_xml_salida():
    url = input("Ingrese una ruta especifica:")
    Lista_senales_temporal.generar_xml_salida(url)
    print("válidado")

def mostrar_Documentarion():
    print("Julio Samuel Isaac Lima Donis")
    print("202200002")
    print("Introducción a la Programación y Computación 2 sección D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to semestre")

def Inicialializar():
    Lista_senales_temporal.eliminar()
    Lista_dato().eliminar()
    lista_grupos().eliminar()
    lista_patrones().eliminar()
    Cargador_Dao_list.eliminar()
    print("eliminado todo... OK!")




def mostrar_menu():
    print("")
    print("")
    print("-------Menú-----------")
    print("1. Cargar archivos")
    print("2. Procesar archivos ")
    print("3. Escribir archivo salida")
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
             generar_xml_salida()
        elif opcion=="5":
            graficar()
        elif opcion=="6":
            Inicialializar()
        elif opcion=="7":
            print("Saliendo del programa, vuevla pronto")
            exit()
        else:
            print("Indique una opción válida")
        mostrar_menu()
            

mostrar_menu()