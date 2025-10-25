# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def email(self, email):
        if '@' not in email:
            raise ValueError('Неверный адрес')

    @property
    def password(self):
       return self.__password

    @password.setter
    def password(self, password):
       self.__password = hash(password)

    def check_password(self, password):
        return self.__password == hash(password)

user = User("test@example.com", "secret")
print(user.email)  # test@example.com
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False