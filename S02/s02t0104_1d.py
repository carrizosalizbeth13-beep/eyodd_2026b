#ELIMINACION  funcion array del modulo array y renombrando como arr

from array import array as arr
#importanto una funcion de otro archivo
from s02t0102_1d import print_array
my_array=arr('i',[2,10,15,20,10])
print ("----- ANTES DE LA ELIMINACION----")
print_array(my_array)
#Eliminacion  

try:
    my_array.remove(100)
except:
    print("⚠️ no se encuentra en el arreglo")
print("----DESPUES DE LA ELIMINACION ---")
print_array(my_array)
