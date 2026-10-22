
from array import array as arr
 # array importa la biblioteca y el segundo es el modulo yb el tercero como lo renombro
 # Parametros de mi  cuadricula
rows= 8
#row_fila 
columns = 2 * rows - 1
# crando el grid  en dos dimensiones 
matrix=[]
#construyendo el grid
for _ in range (rows):
    new_row=arr('i',[0] * columns)
    matrix.append(new_row)

#Validando la construcion del Grid 
print(f"Cantidad de filas :{len (matrix)}")
print(f"Cantidad de columnas de {len (matrix[0])}")

for row in matrix:
    print(list(row))