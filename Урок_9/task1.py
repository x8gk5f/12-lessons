# Задание 1. Количество различных чисел
n = int(input("N: "))
lst = list(map(int, input("Элементы через пробел: ").split()))
print(len(set(lst)))
