# Задание 2. База данных ветеринарной клиники
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_pet(ID):
    return pets[ID] if ID in pets else False

def get_suffix(age):
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

def create():
    if not pets:
        new_id = 1
    else:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    
    name = input("Имя питомца: ")
    p_type = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": p_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Запись добавлена с ID: {new_id}")

def read():
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Неверный ID")
        return
    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден.")
    else:
        name = list(pet.keys())[0]
        info = pet[name]
        p_type = info["Вид питомца"]
        age = info["Возраст питомца"]
        owner = info["Имя владельца"]
        suffix = get_suffix(age)
        print(f'Это {p_type} по кличке "{name}". Возраст питомца: {age} {suffix}. Имя владельца: {owner}')

def update():
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Неверный ID")
        return
    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден.")
    else:
        old_name = list(pet.keys())[0]
        info = pet[old_name]
        
        print("Оставьте поле пустым, если не хотите менять значение.")
        name = input(f"Новое имя ({old_name}): ") or old_name
        p_type = input(f"Новый вид ({info['Вид питомца']}): ") or info["Вид питомца"]
        age_str = input(f"Новый возраст ({info['Возраст питомца']}): ")
        age = int(age_str) if age_str else info["Возраст питомца"]
        owner = input(f"Новый владелец ({info['Имя владельца']}): ") or info["Имя владельца"]
        
        pets[ID] = {
            name: {
                "Вид питомца": p_type,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print("Запись успешно обновлена.")

def delete():
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Неверный ID")
        return
    if ID in pets:
        del pets[ID]
        print("Запись успешно удалена.")
    else:
        print("Питомец с таким ID не найден.")

def pets_list():
    if not pets:
        print("База данных пуста.")
        return
    for ID, pet in pets.items():
        name = list(pet.keys())[0]
        info = pet[name]
        p_type = info["Вид питомца"]
        age = info["Возраст питомца"]
        owner = info["Имя владельца"]
        suffix = get_suffix(age)
        print(f'ID {ID}: Это {p_type} по кличке "{name}". Возраст питомца: {age} {suffix}. Имя владельца: {owner}')

def main():
    command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
    while command != 'stop':
        if command == 'create':
            create()
        elif command == 'read':
            read()
        elif command == 'update':
            update()
        elif command == 'delete':
            delete()
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда.")
        command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()

if __name__ == "__main__":
    main()
