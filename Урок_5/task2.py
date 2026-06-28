# Задание 2. Подсчет букв в слове
word = input("Введите слово из маленьких латинских букв: ")
vowels = "aeiou"
vowels_count = 0
consonants_count = 0
vowel_dict = {v: 0 for v in vowels}

for char in word:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
            vowel_dict[char] += 1
        else:
            consonants_count += 1

print(f"Гласных букв: {vowels_count}")
print(f"Согласных букв: {consonants_count}")

for v in vowels:
    if vowel_dict[v] > 0:
        print(f"Буква '{v}': {vowel_dict[v]}")
    else:
        print(f"Буква '{v}': False")
