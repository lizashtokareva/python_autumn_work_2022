
# todo: Исправить ошибку в коде игры  ../code/ya_kube.py

from lesson_5.code import ya_kube

import random
import uuid
import datetime
from db import DICT_DEFENITION_WORD

name = input("Введите имя:")

def print_menu():
    print("""   
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки 
    """)


print_menu()
num = int(input("Пункт меню:"))


def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()

def save_game(id_session, word, mask):
    f = open('save_game.csv', 'at')
    dt = datetime.datetime.now()
    mask = "".join(mask)
    str = f'{dt} | {id_session} | {name} | {mask} \n'
    f.write(str)
    f.close()
    print('Сохранил игру!')

def load_game(id_session, word, mask):
    f = open('save_game.txt', 'tr')
    indx = 0
    list_str = f.readlines()
    for csv_str in list_str:
        if name in csv_str:
            print(indx, ') ', csv_str)
        indx += 1
    exit(0)


def start_game(session_uuid):
    key = generate_key()
    list_word = list(key)
    mask = ['#'] * len(key)
    print(DICT_DEFENITION_WORD[key])
    print(mask)
    while '#' in mask:
        alfa = input("Введите букву:")
        if alfa == 2:
            print('Сохранение игры')
            save_game(session_uuid, word, mask)
        cnt = 0
        for i in list_word:
            if alfa == i:
                mask[cnt] = alfa
                cnt += 1
                continue
            cnt += 1
        else:
            print(mask)


match num:
    case 1:
        session_uuid = uuid.uuid4()
        start_game()
        # print('The UUID is: ' + str(session_uuid))
    case 2:
        pass
    case 3:
        pass
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще! ")
        pass
