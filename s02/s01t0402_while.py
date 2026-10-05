"""
Escribir un programa que calcule la suma 
de los "n" numeros naturales.
Por ejemplo si n=100, el progrma 
calcula la suma del 1 al 100 
42 usando un ciclo while
"""
#importar la biblioteca de tiempo 
import time
#Crear variables para el problema
n = 100
the_sum = 0
# Tomando el tiempo 1
timestamp_01=time.time()

#Iniciando la suma
while(n > 0):
  the_sum = the_sum + n #100 + 99 + 98 + .. + 1
  n = n - 1

#tomamos el tiemppo2 
timestamp_02 = time.time()

# Imprimimos  la solucion 
print(f"La suma es {the_sum}")

#calculando el tiempo
elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)
print(f"tiempo de eejcucuion: {elapsed_time} us")
