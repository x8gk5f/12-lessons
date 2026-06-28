# Задание 3. Инвесторы
x = float(input("Минимальная сумма инвестиций X: "))
a = float(input("Сумма у Майкла A: "))
b = float(input("Сумма у Ивана B: "))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)
