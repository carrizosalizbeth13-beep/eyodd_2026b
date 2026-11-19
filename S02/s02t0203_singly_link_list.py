# Importando clase Node 
from s02t0201_linked_list import Node
# Crerando la calse  de un lista enlazada
class SinglyList:
    #contructor 
    def __init__(self):
        self.head = None 
    #Metodo de insercion de Nodo en la lista 
    def append (self, data):
        #Creo el nodo 
        new_node = Node (data)
        # si la lista esta vacia apuntamos el head al  nuevo nodo que se creo 
        if not self.head:
            self.head =new_node
            return
        #Si la lista no esta vacia, hay que recorrer al nodo hasta llegar al final de la lista
        # como el primero de la lista
        current_node = self.head
        while current_node.next:
            current_node= current_node.next
         # que hacemos ahora?
        current_node.next = new_node
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
