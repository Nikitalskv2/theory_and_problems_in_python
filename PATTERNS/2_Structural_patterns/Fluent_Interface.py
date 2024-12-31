'''
Основная идея:

- Каждый метод возвращает объект (обычно self), что позволяет вызывать методы в цепочке.
- Это делает код более читаемым и похожим на естественный язык.

Как это работает:

- Person — это класс, который имеет методы для установки имени, возраста и адреса.
- Каждый метод (set_name, set_age, set_address) возвращает self, что позволяет вызывать методы в цепочке.
- str — это метод, который возвращает строковое представление объекта.

Преимущества Fluent Interface:

- Читаемость: Код становится более читаемым и выразительным.
- Удобство: Позволяет вызывать методы в цепочке, что удобно для настройки объектов.
- Гибкость: Можно легко добавлять новые методы в цепочку.

Недостатки:

- Отладка: Может быть сложнее отлаживать код, так как все методы вызываются в одной строке.
- Ограничения: Не всегда подходит для всех типов API, особенно если методы должны возвращать разные типы данных.

Когда использовать:

- Когда нужно сделать API более читаемым и выразительным.
- Когда нужно настраивать объекты с помощью цепочки методов.
- Например, в библиотеках для работы с базами данных, построения запросов, настройки объектов и т.д.

Пример из реальной жизни:

- SQL-запросы: Библиотеки, такие как SQLAlchemy, используют гибкий интерфейс для построения запросов.
- Тестирование: Фреймворки для тестирования, такие как pytest, используют гибкий интерфейс для настройки тестов.
- Конфигурация: Библиотеки для конфигурации, такие как configparser, могут использовать гибкий интерфейс для настройки параметров.
'''


class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.address = None

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_address(self, address):
        self.address = address
        return self

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"


# Создаем объект Person и используем гибкий интерфейс
person = Person().set_name("John Doe").set_age(30).set_address("123 Main St")

# Выводим информацию о человеке
print(person)

# Person(name=John Doe, age=30, address=123 Main St)


# Пример: Гибкий интерфейс для построения SQL-запросов
'''
class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, columns):
        self.query += f"SELECT {columns} "
        return self

    def from_table(self, table):
        self.query += f"FROM {table} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def build(self):
        return self.query.strip()


# Создаем SQL-запрос с использованием гибкого интерфейса

query = QueryBuilder().select("*").from_table("users").where("age > 30").build()
print(query)

# -> SELECT * FROM users WHERE age > 30
'''

# Пример: Гибкий интерфейс для настройки объекта
'''
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def set_make(self, make):
        self.make = make
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_color(self, color):
        self.color = color
        return self

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year}, color={self.color})"


# Создаем объект Car и используем гибкий интерфейс
car = Car().set_make("Toyota").set_model("Camry").set_year(2020).set_color("Blue")
print(car)

# -> Car(make=Toyota, model=Camry, year=2020, color=Blue)
'''
