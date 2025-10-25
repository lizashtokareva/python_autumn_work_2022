# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]

currency = {'USD': 80,
            'EUR': 100,
            'JPY': 1.87,
            '$': 80,
            '€': 100,
            '¥': 1.87,
            'RUB': 1,
            '₽': 1,}

# prices_rubles = [float(''.join(filter(lambda x: x.isdigit() or x =='.', price))) for price in prices if any(symbol in price for symbol in currency.keys())]
prices_updated = [price for price in prices if any(symbol in price for symbol in currency.keys())]
prices_rubles = [currency[any(symbol in price for symbol in currency.keys())]*float(''.join(filter(lambda x: x.isdigit() or x =='.', price))) for price in prices_updated]
