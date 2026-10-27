
from array import array as arr
 # array importa la biblioteca y el segundo es el modulo yb el tercero como lo renombro
 # Parametros de mi  cuadricula
rows= 8
#row_fila 
columns = 2 * rows - 1
# Funcion para imprimir  matrix
def print_matrix(input_matrix):
  for row in matrix:
    print(list(row))


# crando el grid  en dos dimensiones 
matrix=[]
#construyendo el grid
for _ in range (rows):
    new_row=arr('i',[0] * columns)
    matrix.append(new_row)

#Validando la construcion del Grid 
print(f"Cantidad de filas :{len (matrix)}")
print(f"Cantidad de columnas de {len (matrix[0])}")

#calculando en centro de la primera fila 

center = columns // 2 #se hacen diviiones enteras  con doble /
#Estableciendo el centro en 1 
matrix[0][center]
print_matrix(matrix)
#SE calcula el resto de la matrix siguiendo la logica del siperpinsky gasket
for row in range(1,rows):
 for col in range(0,columns):
  left_upper_cell = 0
  right_upper_cell = 0
   #Si la columna donde estamos es mayor a 0
  if col > 0:
    left_upper_cell = matrix[row-1][col-1]
  # si la columna esta un elemento antes del borde derecho
  if col < columns -1:
    right_upper_cell = matrix [row-1][col + 1]
  
  # Guardo el arreglo
  if left_upper_cell != right_upper_cell:
    matrix[row][col]=1
  else:
    matrix[row][col]= 0
print()
print_matrix(matrix)
