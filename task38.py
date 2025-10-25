# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.
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


class Order:
    def __init__(self):
        self.products = []
    def add_product(self, product: Product):
        self.products.append(product)
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
    @property
    def total_price(self):
        return sum(p.price for p in self.products)


# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12