# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

age = int(age)

if foo.isdigit():
    foo = int(foo)

# Преобразуйте переменную age в Boolean
age1 = "123abc"
age1 = bool(age1)
#
# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
#
# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
#
# Преобразуйте значение 0 и 1 в Boolean
zero = bool(0)
one = bool(1)
# Преобразуйте False в строку

str1 = str(False)