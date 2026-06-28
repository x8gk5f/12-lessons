# Задание 3. Переправа рыбаков
m = int(input("Максимальный вес лодки m: "))
n = int(input("Количество рыбаков n: "))
weights = []
for _ in range(n):
    weights.append(int(input()))

weights.sort()

left = 0
right = n - 1
boats = 0

while left <= right:
    if left == right:
        boats += 1
        break
    if weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1

print("Минимальное количество лодок:", boats)
