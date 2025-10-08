# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе



sort_type = int(input('тип сортировки:'))

#Затем сообщение для ввода


match sort_type:
    case 2:
        search_criteria = input('Введите первую букву логина:').upper()
        for user in users:
            if user['login'][0] == search_criteria:
                print(f"Пользователь: '{user['login']}'",  f'возраст {user['age']} года, группа "{user['group']}"')
    case 1:
        search_criteria = int(input('Введите минимальный возраст:'))
        for user in users:
            if user['age'] > search_criteria:
                print(f"Пользователь: '{user['login']}'", f'возраст {user['age']} года, группа "{user['group']}"')
    case 3:
        search_criteria = input('Введите группу:')
        for user in users:
            if user['group'] == search_criteria:
                print(f"Пользователь: '{user['login']}'", f'возраст {user['age']} года, группа "{user['group']}"')

#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"
