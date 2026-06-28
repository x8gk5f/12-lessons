# Задание 1. Словарь питомцев
# По ТЗ: для вывода использовать методы keys() и values()
pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

def get_suffix(age):
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

# Получаем имя питомца через keys(), значения — через values()
name = list(pets.keys())[0]
values = list(pets[name].values())  # [вид, возраст, владелец]

p_type = values[0]
age    = values[1]
owner  = values[2]
suffix = get_suffix(age)

print(f'Это {p_type} по кличке "{name}". Возраст питомца: {age} {suffix}. Имя владельца: {owner}')
