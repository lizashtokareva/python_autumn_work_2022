#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

min_i = -1
min_j = -1
min_dist = len(mass) + 1

for i in range(len(mass)):
    for j in range(i + 1, len(mass)):
        if mass[i] == mass[j] and (j - i) < min_dist:
            min_dist = j - i
            min_i, min_j = i, j
if min_i != -1:
    print(f"Для числа {mass[i]} минимальное растояние в массиве по индексам: {min_i} и {min_j}")
else:
    print(f'Для числа {mass[i]} нет минимального растояния т.к элемент в массиве один.')







