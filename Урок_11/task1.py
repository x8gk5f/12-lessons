# Задание 1. Факториал и список факториалов
def get_factorial(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

MAX_SAFE_INPUT = 7  # factorial(7) = 5040, список из 5040 элементов — приемлемо

num = int(input("Введите число (рекомендуется <= 7): "))
if num < 1:
    print("Ошибка: число должно быть натуральным (>= 1).")
    exit(1)
if num > MAX_SAFE_INPUT:
    print(f"Предупреждение: для числа {num} f({num})={get_factorial(num)}, список будет очень большим.")

f_val = get_factorial(num)
print("Факториал:", f_val)

factorials_list = [get_factorial(i) for i in range(f_val, 0, -1)]

print("Результирующий список:")
print(factorials_list)
