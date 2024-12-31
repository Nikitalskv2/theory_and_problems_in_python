'''

Dependency Injection (DI) — паттерн, в котором зависимости (например, компоненты) обьекта передаются ему извне,
вместо того чтобы объект создавал их самостоятельно.
Это позволяет сделать код более гибким, тестируемым и упрощает управление зависимостями.

Преимущества Dependency Injection:
+ Снижение связанности: Классы зависят от абстракций, а не от конкретных реализаций.
+ Упрощение тестирования: Зависимости можно заменять моками или другими объектами.
+ Улучшение читаемости и расширяемости кода.

'''


class Database:
    def query(self):
        return "Data from Database"


class MockDatabase:
    def query(self):
        return "Mock data for testing"


class Service:
    def __init__(self, database):  # Зависимость передается извне
        self.database = database

    def get_data(self):
        return self.database.query()


# Использование реальной базы данных
real_service = Service(Database())
print(real_service.get_data())  # Data from Database

# Использование моковой базы данных для тестирования
test_service = Service(MockDatabase())
print(test_service.get_data())  # Mock data for testing
# Теперь зависимость Database инъектируется через конструктор Service, что делает код более гибким.


'''
# Пример без Dependency Injection
class Database:
    def query(self):
        return "Data from Database"


class Service:
    def __init__(self):
        self.database = Database()  # Жесткая зависимость

    def get_data(self):
        return self.database.query()


service = Service()
print(service.get_data())
# Проблема: Класс Service жестко связан с реализацией Database. Трудно протестировать Service с подменной базы данных.
'''
