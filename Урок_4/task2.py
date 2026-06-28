# Задание 2. Операции над цифрами пятизначного числа
num = int(input("Введите пятизначное целое число: "))
if 10000 <= abs(num) <= 99999:
    s = str(abs(num))
    d_thousands = int(s[0])
    thousands = int(s[1])
    hundreds = int(s[2])
    tens = int(s[3])
    units = int(s[4])
    
    # Расчет
    denominator = d_thousands - thousands
    if denominator == 0:
        print("Ошибка: цифра десятков тысяч равна цифре тысяч, деление на ноль невозможно.")
    else:
        result = (tens ** units) * hundreds / denominator
        print("Результат:", result)
else:
    print("Число не является пятизначным.")
