"""
s

"""
"""
Escribir un programa que calcule la suma 
de los "n" numeros naturales.
Por ejemplo si n=100, el progrma 
calcula la suma del 1 al 100 
42
"""
#importamos biblioteca time 

import time 
#tomando el tiempo inicial
timestamp_01 = time.time()

# Programa que calcula la suma
# de los "n" numeros naturales 
n=100
total_sum=0
#ciclo for
for number in range(1,n+1):
    #print (number,end=",")
    total_sum = total_sum + number
    #1:sum <- 0 + 1
    # sum =1
    #2: sum<-1+2
    #sum =3
    #3: sum<- 3 + 3
    #...
    #100: sum<- anterior suma + 100

print(f"La suma  de 1 hasta {n} es: {total_sum}")
#tomando el tiempo final 
timestamp_02=time.time()
#impresion del tiempo de ejecucion 
print(f"Tiempo de ejecucion:{(timestamp_02-timestamp_01) * 1e6:.2f} μs")

