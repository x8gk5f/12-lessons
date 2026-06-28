# Задание 1. Подсчет нулей
n = int(input("Введите количество чисел N: "))
zeros = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        zeros += 1
print("Количество нулей:", zeros)
