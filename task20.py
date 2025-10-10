#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().


with open('inverted_sort.txt', 'r') as f:
    lines = f.readlines()

with open('inverted_sort.txt', 'w') as f:
    for line in reversed(lines):
        f.write(line.strip() + '\n')
f.close()