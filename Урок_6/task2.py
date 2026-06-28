# Задание 2. Натуральные делители числа X
import math

x = int(input("Введите натуральное число X: "))
if x < 1:
    print("Ошибка: X должно быть натуральным числом (≥ 1).")
    exit(1)
divisors = 0
limit = int(math.isqrt(x))

for i in range(1, limit + 1):
    if x % i == 0:
        divisors += 1
        if i * i != x:
            divisors += 1

print("Количество делителей:", divisors)
