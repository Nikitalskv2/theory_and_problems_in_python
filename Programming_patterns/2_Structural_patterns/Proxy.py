'''
Основная идея:

- Субъект (Subject) — это интерфейс, который определяет общие операции для реального объекта и заместителя.
- Реальный объект (Real Subject) — это класс, который реализует основные операции.
- Заместитель (Proxy) — это класс, который контролирует доступ к реальному объекту и может добавлять дополнительную логику.

Как это работает:

- Subject — это интерфейс, который определяет общие операции для реального объекта и заместителя.
- RealSubject — это класс, который реализует основные операции.
- Proxy — это класс, который контролирует доступ к реальному объекту и может добавлять дополнительную логику.

Преимущества шаблона Proxy:

- Контроль доступа: Позволяет контролировать доступ к реальному объекту.
- Ленивая инициализация: Позволяет откладывать создание реального объекта до момента его фактического использования.
- Кэширование: Позволяет кэшировать результаты операций реального объекта.
- Гибкость: Позволяет добавлять дополнительную логику без изменения реального объекта.

Недостатки:

- Сложность: Может увеличить сложность кода из-за введения дополнительного класса.
- Производительность: Может привести к дополнительным накладным расходам из-за дополнительной логики.

Когда использовать:

- Когда нужно контролировать доступ к объекту.
- Когда нужно откладывать создание объекта до момента его фактического использования.
- Когда нужно кэшировать результаты операций объекта.
- Например, для ленивой инициализации, контроля доступа, кэширования, логирования и т.д.

Пример из реальной жизни:

- Ленивая инициализация: Заместитель может откладывать создание ресурсоемкого объекта до момента его фактического использования.
- Контроль доступа: Заместитель может проверять права доступа перед выполнением операций.
- Кэширование: Заместитель может кэшировать результаты операций для повышения производительности.
- Логирование: Заместитель может логировать вызовы методов реального объекта.
'''


from abc import ABC, abstractmethod


# Субъект
class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


# Реальный объект
class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


# Заместитель
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")


# Клиентский код
def client_code(subject: Subject) -> None:
    subject.request()


# Создаем реальный объект
real_subject = RealSubject()

# Создаем заместитель и передаем ему реальный объект
proxy = Proxy(real_subject)

# Клиентский код работает с заместителем
client_code(proxy)

# Proxy: Checking access prior to firing a real request.
# RealSubject: Handling request.
# Proxy: Logging the time of request.


# Пример: Ленивая инициализация с использованием Proxy
'''
class HeavyObject:
    def __init__(self):
        print("HeavyObject: Creating a heavy object...")
        self._data = "Heavy data"

    def process(self) -> str:
        return f"HeavyObject: Processing {self._data}"

class LazyProxy:
    def __init__(self):
        self._heavy_object = None

    def process(self) -> str:
        if self._heavy_object is None:
            self._heavy_object = HeavyObject()
        return self._heavy_object.process()

# Клиентский код
proxy = LazyProxy()

# Первый вызов создает тяжелый объект
print(proxy.process())

# Второй вызов использует уже созданный объект
print(proxy.process())

# HeavyObject: Creating a heavy object...
# HeavyObject: Processing heavy data
# HeavyObject: Processing heavy data
'''

# Пример: Контроль доступа с использованием Proxy
'''
class SensitiveData:
    def access_data(self) -> str:
        return "Sensitive data"

class AccessControlProxy:
    def __init__(self, user_role: str):
        self._user_role = user_role
        self._sensitive_data = SensitiveData()

    def access_data(self) -> str:
        if self._user_role == "admin":
            return self._sensitive_data.access_data()
        else:
            return "Access denied"

# Клиентский код
admin_proxy = AccessControlProxy("admin")
user_proxy = AccessControlProxy("user")

print(admin_proxy.access_data())  # Sensitive data
print(user_proxy.access_data())   # Access denied

# Sensitive data
# Access denied
'''