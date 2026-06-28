# Задание 3. Четные числа на отрезке [A, B]
a = int(input("Введите A: "))
b = int(input("Введите B: "))

evens = []
for i in range(a, b + 1):
    if i % 2 == 0:
        evens.append(str(i))

print(" ".join(evens))
