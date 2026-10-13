#importanto el modulo Arrays 
# from array import*
from array import array as arr
#creando un arreglo
# i: entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u:Carácteres inicode qie seran tratados como texto 
my_array = arr('i',[10,22,300,4,8,16,50,320,20,40,27])
# Iterando automaticamente
# for num in my_array:
#     print(num,end=",")
# print()
# #Acceso individual a los elemntos
# print(my_array[0])#Primer elemento
# print(my_array[1])#Segundo elemento
# print(my_array[1])#Tercer elemento

#Tamaño de un arreglo 
#Leng
print(len(my_array))
#Iteracion por índices
# for i in range (len(my_array)):
#     if my_array[i] % 2==0: 
#      print(f"Elemento Num:{i+1}:{my_array[i]}")
# Busqueda de un elemento
num_to_search =200
# Modificando un valor usando backet notation
my_array[7]=200

try:
    print(f"localizando {num_to_search }: {my_array.index(num_to_search)}")
except:
    print("⚠️ Numero no encontrado!!!")
    #try significa probar 
#asignando valor en un indice que no existe
try:
 my_array[100]=3
except:
 print("⚠️ indice no existe!!!")

