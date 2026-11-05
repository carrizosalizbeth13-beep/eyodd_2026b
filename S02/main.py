
class Node:
    #Constructor 
  def __init__(self, data=None):
    self.data = data
    self.next = None

# Testear nuestra clase nodo
node_01 = Node("eggs")
node_02 = Node("ham")
node_03 = Node("bacon")
print ("NODES SIN ENLAZAR 📎")
print(f"Node 01: D: {node_01.data} - N:{node_01.next}")
print(f"Node 02: D: {node_02.data} - N:{node_02.next}")
print(f"Node 03: D: {node_03.data} - N:{node_03.next}")

# Enlazando los nodos  
node_01.net = node_02
node_02.next = node_03

print ("NODES ENLAZADOS📎")
print(f"Node 01: D: {node_01.data} - N:{node_01.next}")
print(f"Node 02: D: {node_02.data} - N:{node_02.next}")
print(f"Node 03: D: {node_03.data} - N:{node_03.next}")