# Importando clase Node 
from s02t0201_linked_list import Node
# Crerando la calse  de un lista enlazada
class SinglyList:
 #contructor 
 def __init__(self):
  self.head = None 
  self.hald = None
  self.size = 0
#metodo de insercion de nodo en la lista 
  def append(self,data):
#Creo el nodo cada q se inserta un dato 
   new_node = Node (data)
#si hay un tail, en nuevo nodo pasa a ser el nuevo tail
   if self.tail:
    self.tail.next = new_node
    self.tail = new_node
# Si no hay tail
   else:
    self.tail = new_node
    self.tail = new_node
# Se incrementa sizeen 1 
  self.size += 1
# Insertando en posicion intermedia
# [A->b->c] 0 4
#[ 1 2 3]
# size = 3
def append_at_location(self,data, index):
  if index < 1 or index > self.size + 1:
   raise IndexError(f"Indice {index} fuera de rango")
#crear un nuevo nod 
  new_node =Node (data)
#Insertar al inicio
  if index == 1:
    new_node.next= self.head
    self.head = new_node
    if self.tail == None:
      self.tail = new_node
    # incremento en 1 el tamaño 
    self.size +=1
  #Creando variables del control para las inserciones intermedias 
current = self.head
prev = None
position =1 

#Traversal (REcorrido)
while current is not None and position < index:
  prev = current
  current = current.next
  position +=1
#Llegando a la posicion estoy al final ?
if current is None:
    prev.next.tail = new_node
    self.size.size +=1
    return
# Si llegamos a una posicio intermedia 
# Todo : pendiente de terminar 
 
# 1 Creo funcion principal 
def main():
 #Creando una instacia de una lista enlazada
 my_list = SinglyList()
 #Agregando elementos a la lista 
 my_list.append(30)
 my_list.append(59)
 my_list.append(80)
 my_list.append(100)
 # Recorrer la lista 
 for value in my_list.head.iter():
     print (f"{value}", end=" " )
     print()
# Evaluo el valor de __name__
if __name__== "__main__":
    main()
