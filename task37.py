# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            self.__price = 0
        else:
            self.__price = price
# Пример использования
product = Product("Book", 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0