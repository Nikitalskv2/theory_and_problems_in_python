'''
!!! примеры смотри в generator_iterator_generator -> generator

Основная идея:

- Компонент (Component) — это интерфейс или абстрактный класс, который определяет общие операции для всех объектов.
- Конкретный компонент (Concrete Component) — это класс, который реализует базовую функциональность.
- Декоратор (Decorator) — это класс, который оборачивает компонент и добавляет новую функциональность, не изменяя его исходный код.

Как это работает:

- Component — это интерфейс, который определяет общие операции для всех объектов.
- ConcreteComponent — это класс, который реализует базовую функциональность.
- Decorator — это класс, который оборачивает компонент и добавляет новую функциональность.
- ConcreteDecoratorA и ConcreteDecoratorB — это конкретные декораторы, которые добавляют свою функциональность.

Преимущества шаблона Decorator:

- Гибкость: Позволяет динамически добавлять функциональность объектам.
- Расширяемость: Можно добавлять новые декораторы, не изменяя существующий код.
- Разделение ответственности: Каждый декоратор отвечает за свою функциональность.

Недостатки:

- Сложность: Может увеличить сложность кода из-за введения множества маленьких классов.
- Ограничения: Не всегда удобно использовать, если функциональность слишком сильно связана с объектом.

Когда использовать:

- Когда нужно динамически добавлять функциональность объектам.
- Когда использование наследования неудобно или невозможно.
- Например, для добавления логирования, кэширования, проверки прав доступа и т.д.

Пример из реальной жизни:

- Логирование: Можно добавить логирование в методы объекта, не изменяя его исходный код.
- Кэширование: Можно добавить кэширование результатов выполнения методов.
- Проверка прав доступа: Можно добавить проверку прав доступа перед выполнением методов.
'''

from abc import ABC, abstractmethod


# Компонент
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретный компонент
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


# Базовый декоратор
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


# Конкретные декораторы
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"


# Клиентский код
def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}")


# Создаем конкретный компонент
simple = ConcreteComponent()
print("Client: I've got a simple component:\n")
client_code(simple)

# Оборачиваем компонент в декораторы
decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print("Client: Now I've got a decorated component:\n")
client_code(decorator2)

'''
Client: I've got a simple component:

RESULT: ConcreteComponent
Client: Now I've got a decorated component:

RESULT: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
'''