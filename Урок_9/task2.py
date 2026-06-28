# Задание 2. Пересечение двух списков
# ТЗ: "Все числа каждого списка находятся на отдельной строке"

n1 = int(input("Количество чисел в первом списке: "))
list1 = set()
for _ in range(n1):
    list1.add(int(input()))

n2 = int(input("Количество чисел во втором списке: "))
list2 = set()
for _ in range(n2):
    list2.add(int(input()))

common = list1.intersection(list2)
print("Количество общих элементов:", len(common))
