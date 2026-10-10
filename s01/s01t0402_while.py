"""
Escribir un programa que calcule la suma 
de los "n" numeros naturales.
Por ejemplo si n=100, el progrma 
calcula la suma del 1 al 100 
42 usando un ciclo while
"""
#importar la biblioteca de tiempo 
import time 
#funcion que suma los primeros "n" numreso naturales
def sum_of_n(n):
    total_sum=0
    #Sumando los "n" numeros 
    #ciclo while
    number=1 
    while number <= n :
      total_sum = total_sum + number
      number = number + 1
      #retornando el total de la suma
    return total_sum
    
#variable para guardar el data set
dataset=[] 
for repetition in range(1,11):
 
 #tomando el tiempo inicial
 timestamp_01 = time.time()
 
 n= repetition*100
 result=sum_of_n(n)
 #tiempo final

 timestamp_02=time.time()
 #calculando el  tiempo
 elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)
 #Agregar la tripleta de los datos al dataset
 dataset.append((n,elapsed_time,result))

for tup in dataset:
  print(tup)
