"""
Generators
los generadores son funciones que pueden pausar su ejecucuion.
Cuando se invoca una funcion generadora devuelve un objeto generador 
(aka Iterador)

El codigo dentro de la funcion  nos ejecuta de inmediato , solo se compila.

La funcion se jecuta unicamnete cuando iteras sobre el generador 
"""
def my_generator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 1
  yield 2
  yield 3
  yield 4
  
#Se invoca funcion generadora  
my_iterador = my_generator()

#Se itera manualmente sobre el generador 
# print(next(my_iterador)) #Imprime 1
# print(next(my_iterador)) #Imprime 2
# print(next(my_iterador)) #Imprime 3
# print(next(my_iterador)) #Imprime 4

# Los indicadores se puede iterar con un for 
for value in my_iterador:
  print(value)