# Задание 1. Переворот массива
n = int(input("Введите количество элементов N: "))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.reverse()
for x in lst:
    print(x)
