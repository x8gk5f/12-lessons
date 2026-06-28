# Задание 2. Сжатие пробелов
# Без использования регулярных выражений — чистая работа со строками
s = input("Введите строку: ")
result = ""
prev_space = False

for char in s:
    if char == ' ':
        if not prev_space:
            result += char
        prev_space = True
    else:
        result += char
        prev_space = False

print(result)
