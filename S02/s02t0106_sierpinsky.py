from array import array as arr
from enum import Enum

def clear_screen():
    print("\033[2J\033[H", end="")

class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Imprime la matriz numérica
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Genera el triángulo de Sierpinski
def generate_triangle(rows=1):

    columns = 2 * rows - 1

    matrix = []

    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)

    center = columns // 2
    matrix[0][center] = 1

    for row in range(1, rows):
        for col in range(columns):

            left_upper_cell = 0
            right_upper_cell = 0

            if col > 0:
                left_upper_cell = matrix[row - 1][col - 1]

            if col < columns - 1:
                right_upper_cell = matrix[row - 1][col + 1]

            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

    return matrix

# Dibuja la matriz
def draw_matrix(input_matrix, symbol="*"):

    for row in input_matrix:
        for cell in row:

            if cell == 1:
                print(
                    AnsiColor.CYAN.value +
                    symbol +
                    AnsiColor.RESET.value,
                    end=""
                )
            else:
                print(
                    AnsiColor.RED.value + " ",
                    end=""
                )

        print()

# Método principal
def main():

    matrix = generate_triangle(15)

    clear_screen()

    draw_matrix(matrix, symbol="■")

if __name__ == "__main__":
    main()
