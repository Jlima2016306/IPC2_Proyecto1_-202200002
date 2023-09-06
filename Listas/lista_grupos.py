from nodos.nodo_grupo import nodo_grupo
import os
class lista_grupos:
  def __init__(self):
    self.primero = None
    self.contador_grupos=0


  def insertar_dato(self,grupo):
    if self.primero is None:
      self.primero = nodo_grupo(grupo=grupo)
      self.contador_grupos+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_grupo(grupo=grupo)
    self.contador_grupos+=1

  def recorrer_e_imprimir_lista(self):
    print("===========================================================================================")
    actual = self.primero
    while actual != None:
      print(" Grupo: ",actual.grupo.el_grupo,"Cadena-grupo: ",actual.grupo.cadena_grupo)
      actual = actual.siguiente
    print("===========================================================================================")


  def generar_graficaBIN(self,nombre_carcel,niveles,celdas_por_nivel):
    f = open('Lectura_xml/bb.dot','w')
    text ="""
        digraph G {"t="""+niveles+"""","A="""+celdas_por_nivel+""""->" """+nombre_carcel+ """" bgcolor="#3990C4" style="filled"
        subgraph cluster1 {fillcolor="blue:red" style="filled"
        node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
        a0 [ label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    actual = self.primero

    while actual != None:

      text+="""<TR>"""  
      text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.grupo.el_grupo) +"""</TD>\n"""

      text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.grupo.cadena_grupo) +"""</TD>\n"""

      text+="""</TR>\n"""  
      actual = actual.siguiente
    text+="""</TABLE>>];
            }
            }\n"""

    f.write(text)
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system('dot -Tpng Lectura_xml/bb.dot -o Lectura_xml/grafo3.png')
    print("terminado")

  def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None  
