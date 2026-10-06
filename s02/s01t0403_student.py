"""
NOTAS:
1.identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2. Es ver cuanto crece el numero de operaciones en mi 
algoritmo conforme creece el tamaño de la entrada
Agrego las  bigO identificadas 
Teniendo en cuenta la Cota superior asintotica
O(n) + O(4)= O(n + 4 )= O(n)
"""
#creando una lista de estudienates 
student_list_01 = ['jordan','pipen','curry','shack']
student_list_02 = ['Mike','Saul','Walter','jessy']

#verificando presencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
      if input_student == student: #O(n)
         print(" ✅ estudiante encontrado") # O(1)
         return student 
  #si  no encuentro al estudiante
    print("❌ estuduante no encontrado")   #O(1) 
    return None 

#Probando algoritmo
check_student("Walter",student_list_01)