#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

vowels = ['а', 'о', 'и', 'у', 'е', 'ё', 'ю', 'я', 'ы', 'э']

with open('dump.txt', 'r') as file:
    content = file.read()
    for letter in vowels:
        if letter in content:
            print(f'Количество букв {letter} - {content.count(letter)}')

