import sys
import os
from nodos.Nodo_dato import Nodo_dato
from Listas.Patron import Patron


class Lista_dato:
  def __init__(self):
    self.primero = None
    self.contador_celdas=0

  def insertar_dato(self,dato):
    if self.primero is None:
      self.primero = Nodo_dato(dato=dato)
      self.contador_celdas+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = Nodo_dato(dato=dato)
    self.contador_celdas+=1

  def insertar_dato_ordenado(self, dato):
        nueva_celda = Nodo_dato(dato=dato)
        self.contador_celdas += 1
        if self.primero is None:
            self.primero = nueva_celda
            return
        if dato.t < self.primero.dato.t or (
                dato.t == self.primero.dato.t and dato.A <= self.primero.dato.A):
            nueva_celda.siguiente = self.primero
            self.primero = nueva_celda
            return
        actual = self.primero
        while actual.siguiente is not None and (
                dato.t> actual.siguiente.dato.t or (
                        dato.t == actual.siguiente.dato.t and dato.A > actual.siguiente.dato.A)):
            actual = actual.siguiente
        nueva_celda.siguiente = actual.siguiente
        actual.siguiente = nueva_celda

  def recorrer_e_imprimir_lista(self):
    print("===========================================================================================")
    actual = self.primero
    while actual != None:
      print(" t: ",actual.dato.t,"A: ",actual.dato.A," Num:",actual.dato.num)
      actual = actual.siguiente
    print("===========================================================================================")


  def devolver_patrones_por_nivel(self,lista_patrones_nivel):
    actual = self.primero
    sentinela_de_filas=actual.dato.t 
    fila_iniciada=False
    recolector_patron=""
    while actual != None:
      if  sentinela_de_filas!=actual.dato.t:
        fila_iniciada=False
        lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
        recolector_patron=""
        sentinela_de_filas=actual.dato.t
      if fila_iniciada==False:
        fila_iniciada=True
        recolector_patron+=str(actual.dato.num)+"-"
      else:
        recolector_patron+=str(actual.dato.num)+"-"
      actual = actual.siguiente
    lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
    print(lista_patrones_nivel)
    return lista_patrones_nivel

  def generar_grafica(self,nombre_carcel,niveles,celdas_por_nivel):
    f = open('Lectura_xml/bb.dot','w')
    text ="""
        digraph G {"t="""+niveles+"""","A="""+celdas_por_nivel+""""->" """+nombre_carcel+ """" bgcolor="#3990C4" style="filled"
        subgraph cluster1 {fillcolor="blue:red" style="filled"
        node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
        a0 [ label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    actual = self.primero
    sentinela_de_filas=actual.dato.t 
    fila_iniciada=False
    while actual != None:
      if  sentinela_de_filas!=actual.dato.t:
        sentinela_de_filas=actual.dato.t
        fila_iniciada=False
        text+="""</TR>\n"""  
      if fila_iniciada==False:
        fila_iniciada=True
        text+="""<TR>"""  
        text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.num) +"""</TD>\n"""
      else:
        text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.num)+"""</TD>\n"""
      actual = actual.siguiente
    text+=""" </TR></TABLE>>];
            }
            }\n"""
    

    f.write(text)
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system('dot -Tpng Lectura_xml/bb.dot -o Lectura_xml/grafo.png')
    print("terminado")



  def devolver_cadena_del_grupo(self,grupo):
    string_resultado=""
    string_temporal=""
    nuevo_cad=""
    buffer=""
    print(grupo)

    for digito in grupo:
      if digito.isdigit():
        buffer+=digito
      else:
        string_temporal=""
        actual = self.primero
        while actual != None:
          if actual.dato.t==int(buffer):            
            kes=False
            vaK= False
            contador=0
            cont=0
            contac=0
            nuevo_cad=""
            pir=0

            for caracter in string_resultado:
              cont+=1

  
              if caracter.isdigit():


                contador += 1   
                if int(contador) == int(contac):
                  contador=pir+1
                  contac=0
                  continue           
                 

                print("contador="+caracter)

                pas = caracter
                print(caracter+"==ddddd==")
       
                caracter=self.nar(string_resultado,cont,pas)
                contac=contador
                if len(caracter)>1:
                  contac=contador+ len(caracter)-1
                  pir=contador
                  print(caracter+"===="+str(len(caracter))+"===="+str(contador)+"====="+str(contac))

                print(str(contador)+":d:" +str(actual.dato.A))


                if contador == int(actual.dato.A) :
                  kes = True
                  print(str(caracter)+":d:" +str(contador)+":"+str(actual.dato.A)+":"+str(actual.dato.num))
                  nuevo_cad += str(int(caracter) + int(actual.dato.num)) 
                else:
                     nuevo_cad += caracter
              else:
                  nuevo_cad += caracter
            if kes == False:
                
                
                string_temporal +=str(actual.dato.num) +","   
                print("finB")
            else: 
                vaK=True     
                print("finA")
                string_resultado=nuevo_cad  
          print("Te")
          actual = actual.siguiente
        if vaK == False:

          string_resultado+=string_temporal
        else:   
          string_resultado=nuevo_cad

        buffer=""
    return string_resultado
  
  def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None 
  def nar(self,string_resultado,contador,caracter):
                  
                  contador2=0
                  contador+=1
                  for caracter2 in string_resultado:
                     contador2+=1
                     if contador2 == contador:
                        if caracter2.isdigit():
                           caracter= str(caracter)+str(caracter2) 
                           return self.nar(string_resultado,contador2,caracter)
                        if caracter2==',':
                           return str(caracter)
                        
                        
  def narC(self,string_resultado,contador,caracter):
                  cont4=0
                  contador2=0

                  for caracter2 in string_resultado:
                     contador2+=1
                     if caracter2.isdigit():
                          cont4+=1
                          if caracter2==caracter:
                            return cont4
                        
    