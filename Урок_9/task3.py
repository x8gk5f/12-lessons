# Задание 3. Повторяющиеся числа
lst = list(map(int, input("Введите числа через пробел: ").split()))
seen = set()
for x in lst:
    if x in seen:
        print("YES")
    else:
        print("NO")
        seen.add(x)
