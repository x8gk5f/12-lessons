# Задание 2. Словарь степеней
my_dict = {}
for i in range(10, -6, -1):
    my_dict[i] = i ** i

for k, v in my_dict.items():
    print(f"{k}: {v}")
