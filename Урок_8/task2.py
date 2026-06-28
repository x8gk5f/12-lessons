# Задание 2. Циклический сдвиг вправо
n = int(input("Количество элементов N: "))
lst = list(map(int, input("Элементы через пробел: ").split()))

if lst:
    lst = [lst[-1]] + lst[:-1]

print(*lst)
