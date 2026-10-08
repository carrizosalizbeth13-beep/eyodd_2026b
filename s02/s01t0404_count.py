# Creamos una lista de estudiantes
# O(1) 
student_list_01 = ['Jordan','Pipen','Curry','Shack','Monrrroy','Arlette','Palestina'] # O(1) 

def random_function(students):
    #acceder al elemento de la lista 
    
    first = students[0] # O(1) 
    total = 0 # O(1)
    #crear una lista vacia me toma # O(1)
    new_list = [] # O(1)

    for student in students:
        print ("se le suma 1 a total")
    #siempre es O(n) si ahi doble for es n al cuadrado
        total += 1 # O (n)
        new_list.append(student) # O(n)
#solo es imprimir 
    print("Imprimiendo estudiantes")
    print(new_list) # O(1)
#regresar el valor
    return total # O (1)
print (f"tamaño de lista:{len(student_list_01)}")

print(random_function(student_list_01))
# Calcular O (2n) + O(5)=O(2n+5)=O(n)