# Задание 1. Сложение случайных матриц
import random

def create_matrix(rows, cols):
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def add_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    m3 = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
    except ValueError:
        print("Неверный ввод. Используем матрицу 10х10.")
        rows, cols = 10, 10
        
    m1 = create_matrix(rows, cols)
    m2 = create_matrix(rows, cols)
    m3 = add_matrices(m1, m2)
    
    print("\nМатрица 1:")
    print_matrix(m1)
    print("\nМатрица 2:")
    print_matrix(m2)
    print("\nРезультат сложения (Матрица 3):")
    print_matrix(m3)

if __name__ == "__main__":
    main()
